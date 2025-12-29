from .llm_interface import LLMInterface
from llm_tools.llm_tools.openai_tools import translator


class OpenAILLM(LLMInterface):
    """
    Implementation of LLMInterface for OpenAI API.
    """

    def __init__(self, model: str):
        """
        Initialize the OpenAI LLM instance.

        :param model: The model to use (e.g., 'gpt-4').  # Change this to your desired OpenAI model.
        # :param api_key: The API key for OpenAI.  # Replace with your OpenAI API key.
        """
        self.model = model

    def translate_text(self, text_to_translate: str, target_language: str) -> str:
        """
        Generate a response using the OpenAI API.

        :param text_to_translate: The text to translate.
        :target_language: The language code to translate the text to
        :return: The generated traduction as a string.
        """
        return translator.translate(text_to_translate, target_language)
