from sqlalchemy.orm import Session
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate
from app.models.user import User
from app.models.category import Category


class CategoryService:
    def __init__(self , db: Session ):
        self.repository = CategoryRepository(db)

    def create_category(self , category_data:CategoryCreate , current_user_id):
            return self.repository.create_category(category_data, user_id= current_user_id)
    
    def get_all_categories(self , current_user_id):
         return self.repository.get_categories(current_user_id)
    
    def get_category_by_id(self, category_id , current_user_id):
         return self.repository.get_category_by_id(category_id, current_user_id)

    def update_category(self , category_id , name: str ,current_user_id): 
         category = self.get_category_by_id(category_id , current_user_id)   
         return self.repository.update_category(category , name, user_id= current_user_id)
    
    def delete_category(self, category_id , current_user_id):
         category = self.get_category_by_id(category_id , current_user_id)
         return self.repository.delete_category(category, user_id=current_user_id)
    

         
    

        