import os

DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://helberth:helberthCO9189@db/taskManagerDB")
SECRET_KEY = os.getenv("SECRET_KEY", "helb_key_task_manager")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30