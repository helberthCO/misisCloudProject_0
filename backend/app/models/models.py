from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from ..database import Base

# SQLAlchemy model for the User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# Pydantic model for creating a new user
class UserCreate(BaseModel):
    name: str
    last_name: str
    username: str
    password: str

# Pydantic model for user login
class UserLogin(BaseModel):
    username: str
    password: str

# Pydantic model for returning user data
class UserSchema(BaseModel):
    id: int
    name: str
    last_name: str
    username: str

    class Config:
        orm_mode = True