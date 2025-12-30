from abc import ABC, abstractmethod


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
