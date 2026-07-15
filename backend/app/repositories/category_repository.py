from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate
from datetime import datetime
from app.models.user import User

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_category( self, category: CategoryCreate , user_id: int):
        new_category = Category()
        new_category.name = category.name
        new_category.user_id = user_id
        new_category.created_at = datetime.now()
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category

    def get_categories(self, user_id: int):
        return (
            self.db.query(Category)
            .filter(Category.user_id == user_id)
            .all()
        )
    
    def get_category_by_id(self , category_id, user_id):
        return (
            self.db.query(Category)
            .filter(Category.id == category_id ,  Category.user_id==user_id)#here , is used instead of 'and' , due to sqlalchemy 
            .first()
        )
    
    def update_category(self , category , name, user_id):
        if category.user_id==user_id:
            category.name=name
        else:
            raise Exception(status_code=403 , detail="Not Authorised")
        self.db.commit()
        self.db.refresh(category)
        return category
    
    def delete_category(self , category, user_id):
        if category.user_id==user_id:
            self.db.delete(category)
        else:
            raise Exception(status_code=403 , detail="Not Authorised")
        self.db.commit()    


