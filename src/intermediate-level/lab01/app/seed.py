from . import crud
from .database import SessionLocal, engine
from .models import Base


def seed():
    Base.metadata.create_all(engine)

    db = SessionLocal()

    user = crud.create_user(db, "Juan", "juan@mail.com")

    order = crud.create_order(db, user)

    crud.add_item(db, order, "Laptop", 1, 1200)

    crud.add_item(db, order, "Mouse", 2, 20)

    db.close()


if __name__ == "__main__":
    seed()
