from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import characters, chats, tokens, memories
from firebase.firebase import initialize

initialize()
app = FastAPI()

@app.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    print("==========================")
    print(request)
    print(exc)
    print("==========================")

    return JSONResponse(
        content={},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )

app.include_router(characters.router, tags=["characters"])
app.include_router(chats.router, tags=["chats"])
app.include_router(tokens.router, tags=["token"])
app.include_router(memories.router, tags=["memory"])
