from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.user_repository import UserRepository
from app.core.jwt import decode_access_token
from fastapi import HTTPException, status


oauth2_scheme= OAuth2PasswordBearer(tokenUrl="/users/login")
async def get_current_user(
        token: Annotated[str , Depends(oauth2_scheme)],
        db: Annotated[Session, Depends(get_db)]
):
    user_repo = UserRepository(db)
    dict_payload = decode_access_token(token) #returns dict from jwt.py (also called 'payload')
    if not dict_payload:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Not Authorized")
    user = user_repo.get_by_email(dict_payload.get("email"))
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized")

    



