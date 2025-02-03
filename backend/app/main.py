from fastapi import FastAPI
from .database import engine, Base
from .views import router as views_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(views_router)

# Create database tables
Base.metadata.create_all(bind=engine)