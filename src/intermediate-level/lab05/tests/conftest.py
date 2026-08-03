import pytest
from app.infrastructure.database import engine
from app.infrastructure.orm_models import Base


@pytest.fixture(autouse=True)
def clean_database():

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield

    Base.metadata.drop_all(engine)
