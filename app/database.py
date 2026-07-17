import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()
Database_Url = os.getenv("DATABASE_URL")

engine = create_engine(Database_Url)
SessionLocal = sessionmaker(bind=engine)
print(Database_Url)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    
