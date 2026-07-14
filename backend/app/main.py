from fastapi import FastAPI

from app.api.health import router as health_router 
from app.api.users import router as users_router
from app.api.category import router as categories_router
from app.core.config import settings

from app.models.user import User
from app.models.category import Category
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)


app= FastAPI(title= settings.app_name)

app.include_router(health_router)
app.include_router(users_router)
app.include_router(categories_router)
# @app.get("/")
# def root():
#     return {"message": "Welcome to Expendo Backend"}