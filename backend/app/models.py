import bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from .database import Base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class UserCreate(BaseModel):
    name: str
    last_name: str
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserSchema(BaseModel):
    id: int
    name: str
    last_name: str
    username: str

    class Config:
        orm_mode = True