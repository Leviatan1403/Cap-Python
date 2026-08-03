import pytest
from app.domain.services import ProductService
from app.infrastructure.database import engine
from app.infrastructure.memory_repository import MemoryRepository
from app.infrastructure.orm_models import Base
from app.infrastructure.sql_repository import SQLRepository

Base.metadata.create_all(engine)


@pytest.mark.parametrize(
    "repository",
    [
        MemoryRepository(),
        SQLRepository(),
    ],
)
def test_lsp(repository):

    service = ProductService(repository)

    service.create_product(10, "Teclado", 200)

    product = service.get_product(10)

    assert product.name == "Teclado"
