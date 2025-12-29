from llm_tools.llm_tools.openai_tools.client_provider import get_client
# TODO: CREATE CONSTRUCTOR TO INITIALIZE THE NEEDED OBJECTS AND INJECT A DEPENDENCY TO KEEP TRACK OF THE TOKENS


def translate(text_to_translate: str, target_language: str, model: str)-> str:
    system_text = f"""
    You are a translator, your goal is to translate any text you get to this language '{target_language}'
    You don't anwser any question or provide additional feedback, the goal is only to translate the text you get, 
    don't include additional text
    """
    # system_text = f"""
    # You are a translator, your goal is to translate any input text to '{target_language}',
    #   * if you don't detect the language of the message return: "Unable to detect original language"
    #   * if you don't detect the target language return: "Unable to translate to language {target_language}". """
    client = get_client()

    response = client.chat.completions.create(
        model=model,
        max_completion_tokens=300,
        messages=[
            {'role': 'system', 'content': system_text},
            {'role': 'user', 'content': text_to_translate}
        ]
    )

    return response.choices[0].message.content

# def translate(text_to_translate: str, target_language: str, model: str, client_provider) -> str:
#     system_text = f"""
#     You are a translator, your goal is to translate any input text to '{target_language}',
#       * if you don't understand what is the original message return: "Unable to detect original language"
#       * if you don't understand what is the target language return: "Unable to translate to language {target_language}".
#     """
#     client = client_provider.get_client()

#     response = client.chat.completions.create(
#         model=model,
#         max_completion_tokens=300,
#         messages=[
#             {'role': 'system', 'content': system_text},
#             {'role': 'user', 'content': text_to_translate}
#         ]
#     )

#     return response.choices[0].message.content