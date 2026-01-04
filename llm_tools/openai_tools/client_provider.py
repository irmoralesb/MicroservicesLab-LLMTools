from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import Optional

# Load environment variables from .env file
load_dotenv()

# Global variable to store the singleton client instance
_client: Optional[OpenAI] = None


def get_client() -> OpenAI:
    """
    Returns a singleton instance of the OpenAI client.
    
    The client is initialized with the API key from the OPENAI_API_KEY
    environment variable. If the client hasn't been created yet, it will be
    instantiated and cached for future calls.
    
    This follows the singleton pattern to reuse the same client instance
    across multiple calls, which is more efficient and recommended by OpenAI.
    
    Returns:
        OpenAI: The OpenAI client instance configured with the API key
        
    Raises:
        ValueError: If OPENAI_API_KEY environment variable is not set
        
    Example:
        >>> client = get_client()
        >>> response = client.chat.completions.create(
        ...     model="gpt-4",
        ...     messages=[{"role": "user", "content": "Hello!"}]
        ... )
    """
    global _client
    if _client is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        _client = OpenAI(api_key=api_key)
    return _client
