import datetime
from pydantic import BaseModel


class BaseObject(BaseModel):
    placement: str
    number_of_the_room: int
    type_of_placement: str
    status: str
    placement_area: float
    floor: int
    living_area: float
    number_of_rooms: str
    total_area: float
    area_without_balconies_loggias: float


class Object(BaseObject):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ObjectIn(BaseObject):
    pass
