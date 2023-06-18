import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
<<<<<<< HEAD

=======
from dotenv import load_dotenv

load_dotenv("../.env", verbose=True)
>>>>>>> f7aaa01b68a78f1151b868e47da0cee295c084e9
api_keys = [os.environ["SERVER_KEY"]]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication

def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Forbidden"
        )