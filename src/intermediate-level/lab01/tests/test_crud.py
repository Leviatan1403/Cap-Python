import app.crud as crud
from app.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:")

TestingSession = sessionmaker(bind=engine)


def test_create_user():
    Base.metadata.create_all(engine)

    db = TestingSession()

    user = crud.create_user(db, "Pedro", "pedro@mail.com")

    assert user.id == 1

    assert user.name == "Pedro"

    db.close()
