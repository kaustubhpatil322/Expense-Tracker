from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.models.user import User


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
    
    def get_all_users(self):
        return self.repository.get_all()
    
    def register_user(self , user_data: UserCreate):
        existing_user = self.repository.get_by_email(user_data.email)
        if existing_user:
            raise ValueError("Email already registered")
        hashed_password = hash_password(user_data.password)
        user = User(
            name=user_data.name,
            email=user_data.email,
            password=hashed_password,
        )
        return self.repository.create(user)
    
    def get_user_by_id(self , user_id: int):
        return self.repository.get_by_id(user_id)
    
    def delete_user_by_id(self , user_id:int):
        return self.repository.delete_by_id(user_id)
      
        
