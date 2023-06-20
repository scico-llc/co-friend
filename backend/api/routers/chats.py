import sys

sys.path.append("../")
from fastapi import APIRouter, Depends
import schemas.chat as sch
import generate_chat.user_chat as chat
from . import auth

router = APIRouter()


@router.post("/chat/setting", dependencies=[Depends(auth.api_key_auth)])
async def set_chat_setting(reqBody: sch.ChatSetting) -> None:
    chat.get_character_setting(
        reqBody.animal_id,
        reqBody.animal_type,
        reqBody.animal_name,
    )

    return


@router.post("/chat", dependencies=[Depends(auth.api_key_auth)])
async def send_chat(reqBody: sch.ChatRequest) -> sch.ChatResponse:
    message = chat.character_chat(reqBody.animal_id, reqBody.message)

    return sch.ChatResponse(
        animal_id=reqBody.animal_id,
        message=message,
    )


@router.post("/chat/topic", dependencies=[Depends(auth.api_key_auth)])
async def send_topic_chat(reqBody: sch.TopicRequest) -> sch.ChatResponse:
    topic = chat.get_topic()
    message = chat.character_chat(reqBody.animal_id, topic, "system")

    return sch.ChatResponse(
        animal_id=reqBody.animal_id,
        message=message,
    )
