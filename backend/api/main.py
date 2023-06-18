from pydantic import BaseModel
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import characters, chats, tokens
from firebase.firebase import initialize
<<<<<<< HEAD
=======
from dotenv import load_dotenv

load_dotenv("../.env", verbose=True)
>>>>>>> f7aaa01b68a78f1151b868e47da0cee295c084e9

initialize()

app = FastAPI()

<<<<<<< HEAD
=======

>>>>>>> f7aaa01b68a78f1151b868e47da0cee295c084e9
@app.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(
        content={},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )

app.include_router(characters.router, tags=["characters"])
app.include_router(chats.router, tags=["chats"])
<<<<<<< HEAD
app.include_router(tokens.router, tags=["token"])
=======
app.include_router(tokens.router, tags=["nft"])
>>>>>>> f7aaa01b68a78f1151b868e47da0cee295c084e9
