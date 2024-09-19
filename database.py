from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base

DATABASE_URL = "sqlite:///./expense_tracker.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
