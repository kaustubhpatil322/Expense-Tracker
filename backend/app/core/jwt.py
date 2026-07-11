from datetime import datetime , timedelta , timezone
from app.core.config import settings
from jose import jwt
from fastapi import HTTPException



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes= int(settings.access_token_expire_minutes))
    to_encode.update({
        "exp":expire
    })

    encoded_jwt = jwt.encode(to_encode , settings.secret_key , algorithm=settings.algorithm)
    return encoded_jwt

def decode_access_token(token: str ):
    payload = jwt.decode(token=token , key=settings.secret_key, algorithms=settings.algorithm)#It return dict
    if payload is None:
        raise HTTPException(status_code=401,detail="Unauthorised")
    else:
        return payload




    
