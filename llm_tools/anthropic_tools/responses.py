from llm_tools.api_response import APIResponse
from anthropic.types import Message
from anthropic.types import TextBlock
import json
import logging 

logger = logging.getLogger(__name__)

class AnthropicTranslatorResponse(APIResponse):
    """
    Response class for translator operations.

    Attributes:
        data (TranslatorResponse.TranslatorData): Contains the translation data.
    """  

    def __init__(self):
        super().__init__()

    @classmethod
    def from_error(cls, code: int, message: str, details: str, error_type: str):
        api_error = cls()
        api_error.is_success = False
        api_error.error.code = code
        api_error.error.message = message
        api_error.error.details = details
        api_error.error.type = error_type
        return api_error


    @classmethod
    def from_success(cls, text_to_translate: str, target_language: str, response: Message):
        """
        Creates a TranslatorResponse instance from a successful ChatCompletion response.

        Args:
            response (ChatCompletion): The ChatCompletion response object.
        """
        logger.info("Running from_success())")
        logger.info(f"Passing {response}")
        api_response = cls()
        api_response.is_success = True

        # Response Data
        content_block = response.content[0]
        if isinstance(content_block, TextBlock):
            content = content_block.text
        else:
            raise ValueError("Response content does not contain text")
        
        inner_data = json.loads(content)

        api_response.data.text_to_translate = text_to_translate
        api_response.data.text_language = inner_data["detected_language"]
        api_response.data.translated_text = inner_data["translated_text"]
        api_response.data.translated_to_language = target_language

        # Tokens
        if response.usage is not None:
            api_response.usage.input_tokens = response.usage.input_tokens
            api_response.usage.output_tokens = response.usage.output_tokens

        return api_response