from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import DATABASE_URI

# # Create the SQLAlchemy engine
engine = create_engine(DATABASE_URI)

# # Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create a Base class for declarative class definitions
Base = declarative_base()