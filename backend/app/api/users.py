from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate , UserResponse
from app.services.user_service import UserService

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