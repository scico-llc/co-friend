from fastapi import FastAPI
from routers import characters, chats, nfts
from firebase.firebase import initialize
from dotenv import load_dotenv

load_dotenv("../.env", verbose=True)

initialize()
app = FastAPI()
app.include_router(characters.router, tags=["characters"])
app.include_router(chats.router, tags=["chats"])
app.include_router(nfts.router, tags=["nft"])