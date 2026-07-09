"""
This file is responsible for:
    1. creating the SQLAlchemy engine
    2. creating a SessionLocal factory
    3. Defining the base class for all your models
    4. Providing a reusable database session dependency for FastAPI
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings



engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(
    autocommit= False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()