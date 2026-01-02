import pytest
from llm_tools.openai_tools.responses import *
from llm_tools.openai_tools.responses import APIResponse, TranslatorResponse

# Add your test cases here


def test_example():
    assert True

# Test cases for APIResponse


class TestAPIResponse:
    def test_error_details_initialization(self):
        error = APIResponse.ErrorDetails()
        assert error.code == 0
        assert error.message == ""
        assert error.details == ""
        assert error.type == ""

    def test_usage_details_initialization(self):
        usage = APIResponse.UsageDetails()
        assert usage.input_tokens == 0
        assert usage.output_tokens == 0

    def test_set_input_tokens(self):
        usage = APIResponse.UsageDetails()
        usage.set_input_tokens(10)
        assert usage.input_tokens == 10

        with pytest.raises(ValueError):
            usage.set_input_tokens(-1)

    def test_set_output_tokens(self):
        usage = APIResponse.UsageDetails()
        usage.set_output_tokens(20)
        assert usage.output_tokens == 20

        with pytest.raises(ValueError):
            usage.set_output_tokens(-5)

    def test_get_total_tokens(self):
        usage = APIResponse.UsageDetails()
        usage.set_input_tokens(10)
        usage.set_output_tokens(15)
        assert usage.get_total_tokens() == 25

# Test cases for TranslatorResponse


class TestTranslatorResponse:
    def test_translator_data_initialization(self):
        data = TranslatorResponse.TranslatorData()
        assert data.text_to_translate == ""
        assert data.text_language == ""
        assert data.translated_text == ""
        assert data.translated_to_language == ""

    def test_set_success(self):
        response = TranslatorResponse()
        response.set_success(
            text_to_translate="Hello",
            text_language="English",
            translated_text="Hola",
            translated_to_language="Spanish"
        )
        assert response.is_success
        assert response.data.text_to_translate == "Hello"
        assert response.data.text_language == "English"
        assert response.data.translated_text == "Hola"
        assert response.data.translated_to_language == "Spanish"

    def test_set_error(self):
        response = TranslatorResponse()
        response.set_error(
            404, "Not Found", "The resource was not found.", "ClientError")
        assert not response.is_success
        assert response.error.code == 404
        assert response.error.message == "Not Found"
        assert response.error.details == "The resource was not found."
        assert response.error.type == "ClientError"
