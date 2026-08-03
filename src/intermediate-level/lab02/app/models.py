from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String, nullable=False)
    product = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(String, default="pending")
