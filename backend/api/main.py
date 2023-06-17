from fastapi import FastAPI
from routers import characters, chats
from firebase.firestore import initialize

initialize()
app = FastAPI()
app.include_router(characters.router, tags=["characters"])
app.include_router(chats.router, tags=["chats"])