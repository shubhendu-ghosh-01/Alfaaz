from models.user_data import UserProfile

class PromptBuilder:
    @staticmethod
    def build_prompt(user: UserProfile, conversation: str) -> str:
        return (
            f"Write a heartfelt Shayri in {user.language} for a person named {user.name}, "
            f"aged {user.age}, with whom the relationship is '{user.relationship}'. "
            f"The Shayri should be based on the recent situation: '{conversation}'. "
            f"Keep it emotionally touching and original."
            f"return only the shayri. Nothing else."
        )
