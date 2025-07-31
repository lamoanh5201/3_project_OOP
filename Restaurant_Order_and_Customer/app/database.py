import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    # Default to SQLite if no DATABASE_URL is provided
    DATABASE_URL = "sqlite:///./restaurant.db"
    print(f"⚠️  No DATABASE_URL found, using default SQLite: {DATABASE_URL}")

# Create engine with appropriate settings
if DATABASE_URL.startswith("sqlite"):
    # SQLite specific settings
    engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
else:
    # PostgreSQL/MySQL settings
    engine = create_engine(DATABASE_URL, echo=False)

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session