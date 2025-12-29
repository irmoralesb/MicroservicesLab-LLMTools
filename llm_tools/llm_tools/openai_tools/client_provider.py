from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
_client: OpenAI = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def get_client() -> OpenAI:

    if not _client:
        raise ReferenceError("Open AI client was not initialized")
    return _client
