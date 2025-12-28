from abc import ABC, abstractmethod

class LLMInterface(ABC):
    """
    Interface for interacting with different LLM APIs.
    """

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the LLM.

        :param prompt: The input prompt for the LLM.
        :return: The generated response as a string.
        """
        pass