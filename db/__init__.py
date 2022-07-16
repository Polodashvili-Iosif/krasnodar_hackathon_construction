from .сonstruction_objects import objects
from .base import metadata, engine

metadata.create_all(bind=engine)
