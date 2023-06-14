from fastapi import APIRouter
router = APIRouter()

@router.post("/chat")
async def send_chat():
    # generate_image("White owl", 10000)
    pass