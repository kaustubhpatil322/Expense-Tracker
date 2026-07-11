from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.user_repository import UserRepository
from app.core.jwt import decode_access_token

app=FastAPI()
oauth2_scheme= OAuth2PasswordBearer(tokenUrl="/login")
async def get_current_user(
        token: Annotated[str , Depends(oauth2_scheme)],
        db: Annotated[Session, Depends(get_db)]
):
    user_repo = UserRepository(db= db)
    dict_payload = decode_access_token(token= token) #returns dict from jwt.py (also called 'payload')
    user = user_repo.get_by_email(dict_payload.get("email"))
    return user

    

    


