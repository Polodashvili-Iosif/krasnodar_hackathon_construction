from typing import List, Optional
import datetime
from models.сonstruction_objects import Object, ObjectIn
from db.сonstruction_objects import objects
from .base import BaseRepository


class ObjectRepository(BaseRepository):

    async def create(self, o: ObjectIn) -> Object:
        object = Object(
            id=0,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            placement=o.placement,
            status=o.status,
            placement_area=o.placement_area,
            floor=o.floor,
            living_area=o.living_area,
            number_of_rooms=o.number_of_rooms,
            total_area=o.total_area,
            area_without_balconies_loggias=o.area_without_balconies_loggias,
        )
        values = {**object.dict()}
        values.pop("id", None)
        query = objects.insert().values(**values)
        object.id = await self.database.execute(query=query)
        return object

    async def update(self, id: int, o: ObjectIn) -> Object:
        object = Object(
            id=id,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            placement=o.placement,
            status=o.status,
            placement_area=o.placement_area,
            floor=o.floor,
            living_area=o.living_area,
            number_of_rooms=o.number_of_rooms,
            total_area=o.total_area,
            area_without_balconies_loggias=o.area_without_balconies_loggias,
        )
        values = {**object.dict()}
        values.pop("id", None)
        values.pop("created_at", None)
        query = objects.update().where(objects.c.id == id).values(**values)
        await self.database.execute(query=query)
        return object

    async def get_all(self, limit: int = 1000, offset: int = 0) -> List[Object]:
        query = objects.select().limit(limit).offset(offset)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = objects.delete().where(objects.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Object]:
        query = objects.select().where(objects.c.id == id)
        job = await self.database.fetch_one(query=query)
        if job is None:
            return None
        return Object.parse_obj(job)
