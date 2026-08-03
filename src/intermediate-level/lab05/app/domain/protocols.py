from typing import Protocol

from .models import Product


class ProductRepository(Protocol):
    def add(self, product: Product) -> None: ...

    def get(self, product_id: int) -> Product | None: ...

    def list(self) -> list[Product]: ...
