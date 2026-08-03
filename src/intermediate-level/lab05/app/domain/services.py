from .models import Product
from .protocols import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, id: int, name: str, price: float):

        if price <= 0:
            raise ValueError("Precio inválido")

        product = Product(id, name, price)

        self.repository.add(product)

    def get_product(self, id: int):

        return self.repository.get(id)

    def list_products(self):

        return self.repository.list()
