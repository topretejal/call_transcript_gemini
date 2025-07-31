import os
from google import genai

from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("GEMINI_API_KEY env variable not set")
        self.client = genai.Client(api_key=api_key)

    def generate_content(self, model: str, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=model,
            contents=[prompt]
        )
        return response.text.strip()

# Singleton instance for reuse in other modules
gemini_client = GeminiClient()
