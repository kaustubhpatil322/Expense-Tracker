from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy.sql import func
from app.db.database import Base
from pydantic import BaseModel , EmailStr


class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True , index=True)
    full_name = Column(String, nullable=False)
    password_hash = Column(String, unique=True , nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class UserCreate(BaseModel):
    full_name:str
    email: EmailStr
    password: str