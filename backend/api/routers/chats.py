from fastapi import FastAPI

app = FastAPI()

@app.post("/chat")
async def send_chat():
    # generate_image("White owl", 10000)
    pass