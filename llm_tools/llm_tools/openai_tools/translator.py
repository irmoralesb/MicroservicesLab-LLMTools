from llm_tools.llm_tools.openai_tools.client_provider import get_client
from llm_tools.llm_tools.openai_tools.Responses import TranslatorResponse
import logging

logger = logging.getLogger(__name__)


def translate(text_to_translate: str, target_language: str, model: str) -> str:
    system_text = f"""
    Act as a translator, follow the next guidelines:

    Rules:
    * Your goal is to translate any text you get to this language '{target_language}'.
    * You have to detect the language of the text to translate and include it in the translated text in English.
    * You don't anwser any question or provide additional feedback, the goal is only to translate the text you get, don't include additional text.

    Example for target_language = spanish:
    text_to_translate: "Tell me what is your name."
    Response: {{"detected_language": "English","translated_text":"Dime cual es tu nombre"}}

    Errors:
    * If you don't detect the language of the input text return this: "Unable to detect original language"
    * If you don't detect the target language return this: "Unable to translate to language {target_language}".  
    """
    logger.info("Running translate function")
    response = TranslatorResponse()

    try:

        logger.info("Getting the API client")
        client = get_client()

        logger.info("Making translation request")
        api_response = client.chat.completions.create(
            model=model,
            max_completion_tokens=300,
            temperature=0,
            messages=[
                {'role': 'system', 'content': system_text},
                {'role': 'user', 'content': text_to_translate}
            ]
        )

        # Checking for errors
        if getattr(api_response, "error", None) is not None:
            logger.error("API call Error.")
            error = api_response.error
            response = TranslatorResponse.from_error(
                code=error.code, message=error.message, details=error.details, error_type=error.type)
            return response

        logger.info("Successful response, parsing data")
        return TranslatorResponse.from_success(text_to_translate, target_language, api_response)
    except Exception as err:
        logger.error(f"Application Error: {str(err)}")
        response = TranslatorResponse.from_error(
            code=500, message="Error processing the request", details=str(err), error_type="application_error")
        return response
