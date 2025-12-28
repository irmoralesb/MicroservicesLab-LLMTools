from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

### TODO: CREATE CONSTRUCTOR TO INITIALIZE THE NEEDED OBJECTS AND INJECT A DEPENDENCY TO KEEP TRACK OF THE TOKENS

def translate(text_to_translate:str, language_to_translate_to: str, model:str):
    system_text = f"""
    You are a translator, your goal is to translate any input text to '{language_to_translate_to}',
      * if you don't undertand what is the original message return: "Unable to detect original language"
      * if you don't understan wha is the target language return: "Unable to translate to language {language_to_translate_to}". """

    response = client.chat.completions.create(
        model=model,
        max_completion_tokens=300,
        messages=[
            {'role':'system', 'content':''},
            {'role':'user', 'content': text_to_translate}
        ]
    )

    return response.choices[0].message.content

