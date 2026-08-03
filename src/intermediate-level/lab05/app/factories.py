from app.infrastructure.memory_repository import MemoryRepository
from app.infrastructure.sql_repository import SQLRepository


def repository_factory(storage: str):

    if storage == "memory":
        return MemoryRepository()

    if storage == "sql":
        return SQLRepository()

    raise ValueError("Repositorio no soportado")
