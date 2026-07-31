from . import crud
from .database import SessionLocal

db = SessionLocal()

users = crud.get_users(db)

for user in users:
    print(user.name)

    for order in user.orders:
        print(order.id)

        for item in order.items:
            print(item.product, item.price)

db.close()
