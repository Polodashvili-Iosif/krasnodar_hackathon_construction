import sqlalchemy
from .base import metadata
import datetime

objects = sqlalchemy.Table(
    "placements",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("placement", sqlalchemy.String),
    sqlalchemy.Column("number_of_the_room", sqlalchemy.Integer),
    sqlalchemy.Column("type_of_placement", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("placement_area", sqlalchemy.Float(precision=2, decimal_return_scale=2)),
    sqlalchemy.Column("floor", sqlalchemy.Integer),
    sqlalchemy.Column("living_area", sqlalchemy.Float(precision=2, decimal_return_scale=2)),
    sqlalchemy.Column("number_of_rooms", sqlalchemy.String),
    sqlalchemy.Column("total_area", sqlalchemy.Float(precision=2, decimal_return_scale=2)),
    sqlalchemy.Column("area_without_balconies_loggias", sqlalchemy.Float(precision=2, decimal_return_scale=2)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)
