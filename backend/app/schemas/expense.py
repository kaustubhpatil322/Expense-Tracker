from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import date

class ExpenseCreate(BaseModel):
    amount: Decimal =Field(gt=0)#= Field(gt=0) — adds a rule: reject zero and negative amounts.
    description: str
    expense_date: date
    category_id:int= Field(gt=0)#this ensures that field must contain '>0' value


