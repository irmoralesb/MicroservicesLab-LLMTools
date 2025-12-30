from llm_tools.llm_tools.openai_tools.client_provider import get_client
import json
# TODO: CREATE CONSTRUCTOR TO INITIALIZE THE NEEDED OBJECTS AND INJECT A DEPENDENCY TO KEEP TRACK OF THE TOKENS

    
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

    client = get_client()

    api_response = client.chat.completions.create(
        model=model,
        max_completion_tokens=300,
        temperature=0,
        messages=[
            {'role': 'system', 'content': system_text},
            {'role': 'user', 'content': text_to_translate}
        ]
    )
    # TODO: CONTINUE HERE, IMPLEMENT THE NEW RESPONSE CLASS FOR TRANSLATOR COMPONENT

    return api_response.choices[0].message.content
