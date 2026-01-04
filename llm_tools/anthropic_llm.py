from .llm_interface import LLMInterface
from llm_tools.anthropic_tools import translator
from llm_tools.api_responses import APIResponse


class AnthropicLLM(LLMInterface):
    """
    Implementation of LLMInterface for Anthropic API.
    """

    def __init__(self, model: str):
        """
        Initialize the Anthropic LLM instance.

        :param model: The model to use (e.g., 'claude-v1').  # Change this to your desired Anthropic model.
        """
        self.model = model

    def translate_text(self, text_to_translate: str, target_language: str) -> APIResponse:
        """
        Generate a response using the Anthropic API.

        :param text_to_translate: The text to translate.
        :target_language: The language code to translate the text to
        :return: The generated traduction as a string.
        """
        return translator.translate(text_to_translate, target_language, self.model)
