from pydantic import BaseModel, Field

class ChatSetting(BaseModel):
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    animal_type: str = Field(None, example="dog")
    animal_name: str = Field(None, example="doggy")

class ChatRequest(BaseModel):
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    message: str = Field(None, example="サンプルメッセージ")

class TopicRequest(BaseModel):
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")

class ChatResponse(BaseModel):
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    message: str = Field(None, example="応答メッセージ")