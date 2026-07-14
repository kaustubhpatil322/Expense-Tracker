from app.db.database import Base
from sqlalchemy import Column, DateTime,Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(Base):#By Inheriting Base class, you're telling SQLAlchemy that this is a DB Model,
                    #Not just a normal Python Class
        __tablename__ = "categories"
        id= Column(Integer,primary_key=True, index=True, unique=True)
        name= Column(String, nullable=False)
        user_id= Column(Integer , ForeignKey("users.id") , nullable=False)
        created_at= Column(DateTime)
        user = relationship("User" , back_populates="categories")
