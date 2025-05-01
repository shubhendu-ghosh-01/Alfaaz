from models.user_data import UserProfile
from core.prompt_builder import PromptBuilder
from utils.gemini_client import GeminiClient

class ShayriService:
    def __init__(self):
        self.client = GeminiClient()

    def generate_shayri(self, user_data: dict, conversation: str) -> str:
        user = UserProfile(**user_data)
        prompt = PromptBuilder.build_prompt(user, conversation)
        return self.client.generate_text(prompt)
