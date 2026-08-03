from app.domain.services import ProductService
from app.infrastructure.database import engine
from app.infrastructure.orm_models import Base
from app.infrastructure.sql_repository import SQLRepository

Base.metadata.create_all(engine)


def test_create_sql():

    repo = SQLRepository()

    service = ProductService(repo)

    service.create_product(2, "Monitor", 400)

    assert service.get_product(2).name == "Monitor"
