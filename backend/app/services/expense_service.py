from sqlalchemy.orm import Session
from app.repositories.expense_repository import ExpenseRepository
from app.schemas.expense import ExpenseCreate
from app.models.expense import Expense
from app.repositories.category_repository import CategoryRepository
from fastapi import HTTPException, status


class ExpenseService:
    def __init__(self, db:Session):
        self.repository = ExpenseRepository(db)
        self.category_repository = CategoryRepository(db)

    def create_expense(self, expense_create: ExpenseCreate , current_user_id):
        new_expense = Expense()
        new_expense.amount = expense_create.amount
        new_expense.description = expense_create.description
        new_expense.expense_date = expense_create.expense_date
        if self.category_repository.get_category_by_id(expense_create.category_id , current_user_id):
            new_expense.category_id = expense_create.category_id#here this is to ensure that category_id sent by the user is Factually present in db or not
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Not Found")
        new_expense.user_id = current_user_id
        return self.repository.create(new_expense)
    
    def get_all_expenses(self , current_user_id):
        return self.repository.get_all(user_id=current_user_id)
    
    def get_expense_by_id(self, expense_id:int , current_user_id: int):
        expense= self.repository.get_by_id(expense_id , current_user_id)
        if expense:
            return expense
        else:
            raise HTTPException(status_code=status.HTTP_404, detail="Item Not Found")
        
    def update_expense(self, expense_create:ExpenseCreate , expense_id:int , current_user_id: int):
        expense = self.get_expense_by_id(expense_id, current_user_id)
        if expense:
            expense.amount = expense_create.amount
            expense.description = expense_create.description
            expense.expense_date=expense_create.expense_date
            expense.category_id=expense_create.category_id
        else:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Item not found")
        
        return self.repository.update(expense)
    
    def delete_expense(self, expense_id:int, current_user_id: int):
        expense = self.get_expense_by_id(expense_id , current_user_id)
        if expense:
            return self.repository.delete(expense)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not Found")
    

    

