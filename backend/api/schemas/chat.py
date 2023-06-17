from typing import Optional, List
from pydantic import BaseModel, Field

class ChatSetting(BaseModel):
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    animal_type: str = Field(None, example="dog")
    animal_name: str = Field(None, example="doggy")

class ChatRequest(BaseModel):
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    message: str = Field(None, example="サンプルメッセージ")