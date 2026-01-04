from anthropic import Anthropic
from dotenv import load_dotenv
import os
from typing import Optional

# Load environment variables from .env file
load_dotenv()

# Global variable to store the singleton client instance
_client: Optional[Anthropic] = None


def get_client() -> Anthropic:
    """
    Returns a singleton instance of the Anthropic client.
    
    The client is initialized with the API key from the ANTHROPIC_API_KEY
    environment variable. If the client hasn't been created yet, it will be
    instantiated and cached for future calls.
    
    This follows the singleton pattern to reuse the same client instance
    across multiple calls, which is more efficient and recommended by Anthropic.
    
    Returns:
        Anthropic: The Anthropic client instance configured with the API key
        
    Raises:
        ValueError: If ANTHROPIC_API_KEY environment variable is not set
        
    Example:
        >>> client = get_client()
        >>> response = client.messages.create(
        ...     model="claude-3-5-sonnet-20241022",
        ...     max_tokens=1024,
        ...     messages=[{"role": "user", "content": "Hello!"}]
        ... )
    """
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
        _client = Anthropic(api_key=api_key)
    return _client
