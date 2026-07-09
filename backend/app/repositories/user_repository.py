from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    def __init__(self , db: Session):
        self.db= db

    def get_all(self ):
        return self.db.query(User).all()
    
    def get_by_email(self , email: str)-> User | None:
        return (
            self.db.query(User) #it acts like "SELECT * FROM USERS"
            .filter(User.email == email)
            .first()
        )

    def create(self , user: User)-> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        
        return user
    
    def get_by_id(self,user_id: int):
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )
    
    def delete_by_id(self, user_id: int):
        existing_user= self.get_by_id(user_id)
        if existing_user:
            self.db.delete(existing_user)
            self.db.commit()
        return existing_user
    


