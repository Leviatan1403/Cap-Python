from app.domain.models import Product

from .database import SessionLocal
from .orm_models import ProductORM


class SQLRepository:
    def add(self, product: Product):

        session = SessionLocal()

        session.add(
            ProductORM(
                id=product.id,
                name=product.name,
                price=product.price,
            )
        )

        session.commit()
        session.close()

    def get(self, product_id):

        session = SessionLocal()

        obj = session.get(ProductORM, product_id)

        session.close()

        if obj is None:
            return None

        return Product(obj.id, obj.name, obj.price)

    def list(self):

        session = SessionLocal()

        rows = session.query(ProductORM).all()

        session.close()

        return [Product(x.id, x.name, x.price) for x in rows]
