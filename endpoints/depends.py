from repositories.сonstruction_objects import ObjectRepository
from db.base import database


def get_object_repository() -> ObjectRepository:
    return ObjectRepository(database)
