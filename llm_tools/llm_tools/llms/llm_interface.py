from abc import ABC, abstractmethod


class LLMInterface(ABC):
    """
    Interface for interacting with different LLM APIs.
    """

    @abstractmethod
    def translate_text(self, text_to_translate: str, target_language: str, model: str) -> str:
        """
        Generate a response from the LLM.

        :param text_to_translate: The text to translate.
        :target_language: The language code to translate the text to
        :return: The generated traduction as a string.
        """
        pass
