from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.expense_service import ExpenseService
from app.schemas.expense import ExpenseCreate
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

def get_expense_service(db: Annotated[Session,  Depends(get_db) ])->ExpenseService:
    return ExpenseService(db)

@router.post("/expense")
def create_expense(expense: ExpenseCreate,
                    expense_service: Annotated[ExpenseService , Depends(get_expense_service) ],
                    current_user:Annotated[User , Depends(get_current_user)]
    ):
    return expense_service.create_expense(expense, current_user.id)

@router.get("/")
def get_all_expenses(current_user:Annotated[User, Depends(get_current_user)],
                    expense_service: Annotated[ExpenseService, Depends(get_expense_service)]):
    return expense_service.get_all_expenses(current_user_id= current_user.id)

@router.get("/{expense_id}")
def get_expense_by_id(expense_id: int,
                      expense_service: Annotated[ExpenseService , Depends(get_expense_service)],
                      current_user: Annotated[User, Depends(get_current_user)]
    ):
    return expense_service.get_expense_by_id(expense_id , current_user_id= current_user.id)

@router.put("/{expense_id}")
def update_expense(
    expense_id: int,
    expense_create: ExpenseCreate,
    expense_service: Annotated[ExpenseService, Depends(get_expense_service)],
    current_user: Annotated[User, Depends(get_current_user)]
):
    return expense_service.update_expense(expense_create , expense_id , current_user_id= current_user.id)
                     

    

        
