import pytest
from unittest.mock import Mock
from anthropic.types import Message, TextBlock, Usage
from llm_tools.anthropic_tools.responses import AnthropicTranslatorResponse
from llm_tools.api_responses import APIResponse
import json

from llm_tools.openai_tools.responses import OpenAITranslatorResponse


# Test cases for AnthropicTranslatorResponse
        
class TestAnthropicTranslatorResponse:
    def test_initialization(self):
            response = AnthropicTranslatorResponse()
            assert response.is_success is False
            assert isinstance(response.error, APIResponse.ErrorDetails)
            assert isinstance(response.usage, APIResponse.UsageDetails)
            assert isinstance(response.data, APIResponse.TranslatorData)

    def test_set_success(self):
        response = AnthropicTranslatorResponse()
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
        response = AnthropicTranslatorResponse()
        response.set_error(
            404, "Not Found", "The resource was not found.", "ClientError")
        assert not response.is_success
        assert response.error.code == 404
        assert response.error.message == "Not Found"
        assert response.error.details == "The resource was not found."
        assert response.error.type == "ClientError"

    def test_from_error(self):
        response = AnthropicTranslatorResponse.from_error(
            code=500,
            message="Internal Server Error",
            details="Something went wrong",
            error_type="ServerError"
        )
        assert response.is_success is False
        assert response.error.code == 500
        assert response.error.message == "Internal Server Error"
        assert response.error.details == "Something went wrong"
        assert response.error.type == "ServerError"

    def test_from_success_with_text_block(self):
        # Create mock Message with TextBlock
        mock_usage = Mock(spec=Usage)
        mock_usage.input_tokens = 100
        mock_usage.output_tokens = 50

        mock_text_block = Mock(spec=TextBlock)
        mock_text_block.text = json.dumps({
            "detected_language": "English",
            "translated_text": "Hola"
        })

        mock_message = Mock(spec=Message)
        mock_message.content = [mock_text_block]
        mock_message.usage = mock_usage

        response = AnthropicTranslatorResponse.from_success(
            text_to_translate="Hello",
            target_language="Spanish",
            response=mock_message
        )

        assert response.is_success is True
        assert response.data.text_to_translate == "Hello"
        assert response.data.text_language == "English"
        assert response.data.translated_text == "Hola"
        assert response.data.translated_to_language == "Spanish"
        assert response.usage.input_tokens == 100
        assert response.usage.output_tokens == 50

    def test_from_success_without_usage(self):
        # Create mock Message without usage
        mock_text_block = Mock(spec=TextBlock)
        mock_text_block.text = json.dumps({
            "detected_language": "French",
            "translated_text": "Bonjour"
        })

        mock_message = Mock(spec=Message)
        mock_message.content = [mock_text_block]
        mock_message.usage = None

        response = AnthropicTranslatorResponse.from_success(
            text_to_translate="Hi",
            target_language="French",
            response=mock_message
        )

        assert response.is_success is True
        assert response.data.text_language == "French"
        assert response.data.translated_text == "Bonjour"
        assert response.usage.input_tokens == 0
        assert response.usage.output_tokens == 0

    def test_from_success_invalid_response_content(self):
        # Create mock Message with non-TextBlock content
        mock_non_text_block = Mock()
        mock_message = Mock(spec=Message)
        mock_message.content = [mock_non_text_block]

        with pytest.raises(ValueError, match="Response content does not contain text"):
            AnthropicTranslatorResponse.from_success(
                text_to_translate="Hello",
                target_language="Spanish",
                response=mock_message
            )
