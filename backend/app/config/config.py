import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Database connection URI
DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://helberth:helberthCO9189@db:5432/taskManagerDB")

# Secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY", "helb_key_task_manager")

# Algorithm used for JWT
ALGORITHM = "HS256"

# Access token expiration time in minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30