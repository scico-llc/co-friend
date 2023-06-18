import sys

sys.path.append("../")
from fastapi import APIRouter
import schemas.chat as sch
import generate_chat.user_chat as chat

router = APIRouter()


@router.post("/chat")
async def send_chat(reqBody: sch.ChatRequest) -> sch.ChatResponse:
    message = chat.character_chat(
        reqBody.animal_id,
        reqBody.message,
    )

    return sch.ChatResponse(reqBody.animal_id, message)


@router.post("/chat/setting")
async def send_chat(reqBody: sch.ChatSetting):
    chat.get_character_setting(
        reqBody.animal_id,
        reqBody.animal_type,
        reqBody.animal_name,
    )

    return