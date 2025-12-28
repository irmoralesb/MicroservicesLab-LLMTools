from .llm_interface import LLMInterface
import openai

class OpenAILLM(LLMInterface):
    """
    Implementation of LLMInterface for OpenAI API.
    """

    def __init__(self, model: str, api_key: str):
        """
        Initialize the OpenAI LLM instance.

        :param model: The model to use (e.g., 'gpt-4').  # Change this to your desired OpenAI model.
        :param api_key: The API key for OpenAI.  # Replace with your OpenAI API key.
        """
        self.model = model
        self.api_key = api_key
        openai.api_key = api_key

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response using the OpenAI API.

        :param prompt: The input prompt for the LLM.
        :return: The generated response as a string.
        """
        response = openai.ChatCompletion.create(  # Adjust parameters as needed for your use case.
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']