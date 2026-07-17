from sqlalchemy.orm import Session
from app.models.expense import Expense
from fastapi import HTTPException, status
class ExpenseRepository:
    def __init__(self, db:Session):
        self.db = db

    def create(self, expense: Expense )->Expense:
        self.db.add(expense)
        self.db.commit()
        self.db.refresh(expense)
        return expense
    
    def check_user_id(self,Curre)
    
    def get_all(self , user_id:int):
        return (
            self.db.query(Expense)
            .filter(Expense.user_id == user_id)
            .all()
        )

    def get_all_by_category_id(self, category_id:int , user_id:int):
        return (self.db.query(Expense)
                .filter(Expense.category_id == category_id, Expense.user_id == user_id)
                .all()
                )

    def get_by_id(self, expense_id:int , user_id:int):
        return (
            self.db.query(Expense)
            .filter(Expense.id == expense_id , Expense.user_id==user_id)
            .first()
        )
    
    def update(self,expense:Expense):
        self.db.commit()
        self.db.refresh(expense)
        return expense
    
    def delete(self, expense:Expense):
        self.db.delete(expense)
        self.db.commit()
        return expense
    
        
            

        
        

    
