from pydantic import BaseModel
from datetime import datetime


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass
    
class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime

    model_config={
        "from_attributes":True
    }