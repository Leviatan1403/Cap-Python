import os

from app.database import Base
from app.dependencies import get_db
from app.main import app
from app.models import User
from app.security import hash_password
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if os.path.exists("test.db"):
    os.remove("test.db")

# Base de datos en memoria
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def create_test_user():
    db = TestingSessionLocal()

    user = User(username="admin", hashed_password=hash_password("admin123"))

    db.add(user)
    db.commit()
    db.close()


create_test_user()
