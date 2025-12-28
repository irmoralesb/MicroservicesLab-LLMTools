from .openai_llm import OpenAILLM
from .anthropic_llm import AnthropicLLM
from .llm_interface import LLMInterface

class LLMFactory:
    """
    Factory class to create LLM instances.
    """

    @staticmethod
    def create_llm(provider: str, model: str, api_key: str) -> LLMInterface:
        """
        Create an LLM instance based on the provider.

        :param provider: The LLM provider ('openai' or 'anthropic').  # Ensure the provider matches your setup.
        :param model: The model to use.  # Specify the model supported by the provider.
        :param api_key: The API key for the provider.  # Replace with the correct API key.
        :return: An instance of LLMInterface.
        """
        if provider.lower() == 'openai':
            return OpenAILLM(model, api_key)
        elif provider.lower() == 'anthropic':
            return AnthropicLLM(model, api_key)
        else:
            raise ValueError(f"Unsupported provider: {provider}")