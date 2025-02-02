from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import timedelta
from .database import SessionLocal, engine
from .models import Base, UserCreate, UserLogin
from .crud import get_user_by_username, create_user
from .auth import verify_password, create_access_token

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario ya registrado, por favor inicia sesión",
        )
    create_user(db, user.name, user.last_name, user.username, user.password)
    return {"message": "Usuario registrado exitosamente"}

@app.post("/login")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user.username)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no registrado, por favor regístrate",
        )
    if not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta",
        )
    access_token_expires = timedelta(minutes=1)
    access_token = create_access_token(
        data={"sub": existing_user.username}, expires_delta=access_token_expires
    )
    user_data = {
        "username": existing_user.username,
        "name": existing_user.name,
        "last_name": existing_user.last_name,
        "access_token": access_token,
        "token_type": "bearer"
    }
    return user_data