# MicroservicesLab-LLMTools
Tools to call OpenAI and Anthropic APIs via a simple interface.

## Installation
- From source (editable):
	```bash
	pip install -e .
	```
- Or add to your project requirements:
	```
	llm_tools @ git+https://github.com/irmoralesb/MicroservicesLab-LLMTools.git
	```

## Requirements
- Python 3.7+
- Environment variables:
	- `OPENAI_API_KEY` for OpenAI usage
	- `ANTHROPIC_API_KEY` for Anthropic usage

## Quick Start
```python
from llm_tools import LLMFactory

# Create an LLM client
llm = LLMFactory.create_llm(provider="openai", model="gpt-4o-mini")

# Translate text
resp = llm.translate_text("Hello, world!", target_language="spanish")

if resp.is_success:
		print("Detected:", resp.data.text_language)
		print("Translated:", resp.data.translated_text)
else:
		print("Error:", resp.error.message, resp.error.details)
```

## Development
- Install dev deps:
	```bash
	pip install -r requirements.txt
	```
- Run tests:
	```bash
	pytest -q
	```
