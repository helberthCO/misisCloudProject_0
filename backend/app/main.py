from .database import engine, Base
from .views import app

Base.metadata.create_all(bind=engine)