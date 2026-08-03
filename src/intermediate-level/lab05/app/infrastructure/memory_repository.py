from app.domain.models import Product


class MemoryRepository:
    def __init__(self):
        self.products = {}

    def add(self, product: Product):

        self.products[product.id] = product

    def get(self, product_id: int):

        return self.products.get(product_id)

    def list(self):

        return list(self.products.values())
