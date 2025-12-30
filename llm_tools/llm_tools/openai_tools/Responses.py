from abc import ABC, abstractmethod
from openai import ChatCompletion
import json
import logging

logger = logging.getLogger(__name__)

class APIResponse(ABC):
    """
    Abstract base class for API responses.
    All responses must use this base class for consistency, 

    Attributes:
        is_success (bool): Indicates if the API call was successful.
        error (APIResponse.ErrorDetails): Contains error details if the API call failed.

    Functions:
        set_success(self): Implemented by the child class to set the custom response data.
    """

    def __init__(self):
        self.is_success: bool = False
        self.error = self.ErrorDetails()
        self.usage = self.UsageDetails()

    class ErrorDetails:
        """
        Class to encapsulate error details.

        Attributes:
            code (int): Error code.
            message (str): Error message.
            details (str): Additional error details.
            type (str): Type of the error.
        """

        def __init__(self):
            self.code: int = 0
            self.message: str = ""
            self.details: str = ""
            self.type: str = ""

    class UsageDetails:
        """
        Class to encapsulate usage details for API responses.

        Attributes:
            input_tokens (int): Number of input tokens used.
            output_tokens (int): Number of output tokens generated.
        """

        def __init__(self):
            self.input_tokens: int = 0
            self.output_tokens: int = 0

        def set_input_tokens(self, token_number: int) -> None:
            if token_number < 0:
                raise ValueError(
                    f"Invalid input token number {token_number}: must be zero or positive.")

            self.input_tokens = token_number

        def set_output_tokens(self, token_number: int) -> None:
            if token_number < 0:
                raise ValueError(
                    f"Invalid output token number {token_number}: must be zero or positive.")

            self.output_tokens = token_number

        def get_total_tokens(self) -> int:
            return self.input_tokens + self.output_tokens

    @abstractmethod
    def set_success(self):
        """
        Abstract method to set the success state of the response.
        Must be implemented by subclasses.
        """
        pass

    def set_error(self, code: int = -1, message: str = "", details: str = "", type: str = ""):
        """
        Sets the error details for the response.

        Args:
            code (int): Error code. Defaults to -1.
            message (str): Error message. Defaults to an empty string.
            details (str): Additional error details. Defaults to an empty string.
            type (str): Type of the error. Defaults to an empty string.
        """
        self.is_success = False
        self.error.code = code
        self.error.message = message
        self.error.details = details
        self.error.type = type


class TranslatorResponse(APIResponse):
    """
    Response class for translator operations.

    Attributes:
        data (TranslatorResponse.TranslatorData): Contains the translation data.
    """

    def __init__(self):
        super().__init__()
        self.data = self.TranslatorData()

    class TranslatorData:
        """
        Class to encapsulate translation data.

        Attributes:
            text_to_translate (str): The original text to be translated.
            text_language (str): The language of the original text.
            translated_text (str): The translated text.
            translated_to_language (str): The language to which the text was translated.
        """

        def __init__(self):
            self.text_to_translate: str = ""
            self.text_language: str = ""
            self.translated_text: str = ""
            self.translated_to_language: str = ""

    def set_success(self, text_to_translate: str, text_language: str, translated_text: str, translated_to_language: str):
        """
        Sets the success state and translation data for the response.

        Args:
            text_to_translate (str): The original text to be translated.
            text_language (str): The language of the original text.
            translated_text (str): The translated text.
            translated_to_language (str): The language to which the text was translated.
        """
        self.is_success = True
        self.data.text_to_translate = text_to_translate
        self.data.text_language = text_language
        self.data.translated_text = translated_text
        self.data.translated_to_language = translated_to_language

    @classmethod
    def from_error(cls, code: int, message: str, details: str, error_type: str):
        api_error = cls()
        api_error.is_success = False
        api_error.error.code = code
        api_error.error.message = message
        api_error.error.details = details
        api_error.error.type = error_type

    @classmethod
    def from_success(cls, text_to_translate: str, target_language: str, response: ChatCompletion):
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
        inner_data = json.loads(response.choices[0].message.content)

        api_response.data.text_to_translate = text_to_translate
        api_response.data.text_language = inner_data["detected_language"]
        api_response.data.translated_text = inner_data["translated_text"]
        api_response.data.translated_to_language = target_language

        # Tokens
        api_response.usage.input_tokens = response.usage.prompt_tokens
        api_response.usage.output_tokens = response.usage.completion_tokens

        return api_response
