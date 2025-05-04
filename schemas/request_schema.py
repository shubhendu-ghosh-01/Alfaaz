from pydantic import BaseModel
from typing import Optional

class ShayriRequest(BaseModel):
    name: str
    age: int
    relationship: str
    language: str
    latest_conversation: dict
