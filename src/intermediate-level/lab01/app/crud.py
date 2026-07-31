from .models import Order, OrderItem, User


def create_user(db, name, email):
    user = User(name=name, email=email)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users(db):
    return db.query(User).all()


def create_order(db, user):
    order = Order(user=user)

    db.add(order)

    db.commit()

    db.refresh(order)

    return order


def add_item(db, order, product, qty, price):
    item = OrderItem(order=order, product=product, quantity=qty, price=price)

    db.add(item)

    db.commit()

    db.refresh(item)

    return item
