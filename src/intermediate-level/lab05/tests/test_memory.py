from app.domain.services import ProductService
from app.infrastructure.memory_repository import MemoryRepository


def test_create_memory():

    repo = MemoryRepository()

    service = ProductService(repo)

    service.create_product(1, "Laptop", 100)

    assert service.get_product(1).name == "Laptop"
