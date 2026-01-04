from llm_tools.api_responses import APIResponse
import pytest

# Test cases for APIResponse

class TestAPIResponse:
    def test_translator_data_initialization(self):
        data = APIResponse.TranslatorData()
        assert data.text_to_translate == ""
        assert data.text_language == ""
        assert data.translated_text == ""
        assert data.translated_to_language == ""

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