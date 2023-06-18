import sys

sys.path.append("../")
from fastapi import APIRouter, Depends
import schemas.chat as sch
import generate_chat.user_chat as chat
from . import auth

router = APIRouter()

@router.post("/chat", dependencies=[Depends(auth.api_key_auth)])
async def send_chat(reqBody: sch.ChatRequest) -> sch.ChatResponse:
    message = chat.character_chat(
        reqBody.animal_id,
        reqBody.message,
    )

    return sch.ChatResponse(reqBody.animal_id, message)


@router.post("/chat/setting", dependencies=[Depends(auth.api_key_auth)])
async def send_chat(reqBody: sch.ChatSetting):
    chat.get_character_setting(
        reqBody.animal_id,
        reqBody.animal_type,
        reqBody.animal_name,
    )

    return
