import requests
from config import settings

class GeminiClient:
    def __init__(self, api_key: str = settings.GEMINI_API_KEY):
        self.api_key = api_key
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

    def generate_text(self, prompt: str) -> str:
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        response = requests.post(
            f"{self.base_url}?key={self.api_key}",
            json=payload,
            headers=headers
        )

        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        else:
            raise Exception(f"Gemini API Error: {response.status_code}, {response.text}")
