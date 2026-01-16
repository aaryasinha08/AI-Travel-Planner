

import os
import requests
from dotenv import load_dotenv

# Load variables from .env file (local development)
load_dotenv()

# Hugging Face Chat Completion API
API_URL = "https://router.huggingface.co/v1/chat/completions"

# Securely fetch API token
HF_API_KEY = os.getenv("HF_TOKEN")

# Safety check
if not HF_API_KEY:
    raise EnvironmentError(
        "HF_TOKEN not found. Please set it in .env file or environment variables."
    )

# Request headers
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


def ask_ai(user_query: str) -> str:
    """
    Sends user query to Hugging Face LLM and returns AI response.

    Parameters:
        user_query (str): User's input message

    Returns:
        str: AI-generated response
    """

    if not user_query or not user_query.strip():
        return "⚠️ Empty message sent to AI."

    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": user_query.strip()
            }
        ]
    }

    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            timeout=60
        )

        # Handle API errors
        if response.status_code != 200:
            return (
                f"❌ API Error ({response.status_code}): "
                f"{response.text}"
            )

        data = response.json()

        # Extract response safely
        return data["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "❌ Request timed out. Please try again."

    except requests.exceptions.RequestException as e:
        return f"❌ Network error: {str(e)}"

    except (KeyError, IndexError):
        return "❌ Unexpected response format from AI."

