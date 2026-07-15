from app.db.database import Base
from sqlalchemy import Numeric, Column, Text, Date, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Expense(Base):
    __tablename__="expenses"
    id= Column(Integer, primary_key=True , index=True)
    amount= Column(Numeric(12,2) , nullable=False)
    description= Column(Text, nullable=True)
    expense_date= Column(Date, nullable=False)
    user_id = Column(Integer , ForeignKey("users.id"), nullable=False)
    category_id= Column(Integer, ForeignKey("categories.id"), nullable=False)
    user = relationship("User" , back_populates="expenses")
    category = relationship("Category" , back_populates="expenses")# one category-> Many expenses
    created_at= Column(DateTime(timezone=True), server_default= func.now())
    #server_default=func.now() --> PostgreSQL itself fills the column with the current time automatically.
