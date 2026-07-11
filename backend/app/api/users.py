from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate , UserResponse, UserLogin
from app.services.user_service import UserService
from app.core.dependencies import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/users",
    tags = ["Users"]
)


def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)

@router.get("/")
def get_users(
    service: UserService = Depends(get_user_service)
):
    return service.get_all_users()

@router.get("/me")#current user
def get_me(
    current_user: Annotated[User , Depends(get_current_user)]#Alternante and cleaner way of writing -  "Sesion= Depends(get_db)"
):
    return current_user

@router.get("/{user_id}")
def get_user_by_user_id(
    user_id: int,
    service: UserService=Depends(get_user_service), 
):
    return service.get_user_by_id(user_id)

@router.delete("/{user_id}")
def delete_user_by_user_id(
    user_id: int,
    service: UserService=Depends(get_user_service),
):
    return service.delete_user_by_id(user_id)

@router.post(
    "/register",
    response_model=UserResponse
)
def register_user(
    user_data: UserCreate,
    db: Session= Depends(get_db),
):
    service = UserService(db)
    return service.register_user(user_data)

@router.post("/login")
def login_user(
    form_data:OAuth2PasswordRequestForm=Depends(),# Ask FastAPI to create an OAuth2PasswordRequestForm object
                                        # by reading the incoming form data (username, password, etc.)
                                        # and inject that object into this function.
    db: Session= Depends(get_db),                  
):
    service = UserService(db)
    login_data= UserLogin(
        email = form_data.username,
        password = form_data.password
    )
    return service.login_user(login_data)

    
