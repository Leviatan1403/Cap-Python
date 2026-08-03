from app.domain.services import ProductService
from app.factories import repository_factory
from app.infrastructure.database import engine
from app.infrastructure.orm_models import Base

Base.metadata.create_all(engine)

# repo = repository_factory("memory")

repo = repository_factory("sql")

service = ProductService(repo)

service.create_product(1, "Laptop", 30000)

service.create_product(2, "Mouse", 500)

for product in service.list_products():
    print(product)
