from llm_tools.anthropic_tools.client_provider import get_client
from llm_tools.anthropic_tools.responses import AnthropicTranslatorResponse
import logging

logger = logging.getLogger(__name__)


def translate(text_to_translate: str, target_language: str, model: str) -> AnthropicTranslatorResponse:
    system_message = """
Act as a translation tool, NOT a conversational assistant.

CRITICAL RULES:
* You MUST respond ONLY with valid JSON, no other text.
* You MUST detect the language of the input text.
* You MUST translate the text to Spanish only.
* You MUST NOT engage in conversation or ask for clarification.
* You MUST NOT include any text outside the JSON structure.

Response format (REQUIRED):
{"detected_language": "LANGUAGE_NAME", "translated_text": "TRANSLATED_TEXT_HERE"}

Error responses (use ONLY if applicable):
* If language detection fails: {"error": "Unable to detect original language"}
* If translation fails: {"error": "Unable to translate to language Spanish"}

Example:
Input: "Tell me what is your name."
Output: {"detected_language": "English", "translated_text": "Dime cuál es tu nombre"}

Remember: RESPOND ONLY WITH JSON. NO OTHER TEXT.
"""
    logger.info("Running translate function")

    try:
        logger.info("Getting the API client")
        client = get_client()

        logger.info("Making translation request")
        api_response = client.messages.create(
            model=model,
            max_tokens=1024,
            system=system_message,
            messages=[
                {'role': 'user', 'content': text_to_translate}
            ]
        )
        logger.info("Successful response, parsing data")
        return AnthropicTranslatorResponse.from_success(text_to_translate, target_language, api_response)
    except Exception as err:
        logger.error(f"Application Error: {str(err)}")
        response = AnthropicTranslatorResponse.from_error(
            code=500, message="Error processing the request", details=str(err), error_type="application_error")
        return response
