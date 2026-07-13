from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.database import get_db
from app.services.category_service import CategoryService
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.category import CategoryCreate


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

def get_category_service(db: Annotated[Session , Depends(get_db)]):
    return CategoryService(db)



@router.get("/")
def get_categories(
    current_user: Annotated[User , Depends(get_current_user)],
    category_service: Annotated[CategoryService , Depends(get_category_service)]
    ):
    return category_service.get_all_categories(current_user.id)

@router.post("/category")
def create_category(
    category: CategoryCreate,
    category_service: Annotated[CategoryService, Depends(get_category_service)],
    current_user: Annotated[User, Depends(get_current_user)]
):
    return category_service.create_category(category ,current_user_id= current_user.id )

@router.get("/{category_id}")
def get_category_by_id(
    category_id: int,
    category_service: Annotated[CategoryService , Depends(get_category_service)],
    current_user: Annotated[User , Depends(get_current_user)]
):
    return category_service.get_category_by_id(category_id , current_user_id=current_user.id)

@router.put("/{category_id}")
def update_category(
    category_id: int,
    category: CategoryCreate,
    category_service: Annotated[CategoryService , Depends(get_category_service)],
    current_user: Annotated[User , Depends(get_current_user)]
):
    return category_service.update_category(category_id ,name=category.name,current_user_id=current_user.id)

@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    category_service: Annotated[CategoryService, Depends(get_category_service)],
    current_user: Annotated[User , Depends(get_current_user)]
):
    return category_service.delete_category(category_id ,current_user_id=current_user.id )

    