from typing import List
from models.сonstruction_objects import Object, ObjectIn
from repositories.сonstruction_objects import ObjectRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_object_repository

router = APIRouter()


@router.get("/", response_model=List[Object])
async def read_objects(
        limit: int = 1000,
        offset: int = 0,
        objects: ObjectRepository = Depends(get_object_repository)):
    return await objects.get_all(limit=limit, offset=offset)


@router.post("/", response_model=Object)
async def create_object(
        o: ObjectIn,
        objects: ObjectRepository = Depends(get_object_repository)):
    return await objects.create(o=o)


@router.put("/", response_model=Object)
async def update_object(
        id: int,
        o: ObjectIn,
        objects: ObjectRepository = Depends(get_object_repository)):
    object = await objects.get_by_id(id=id)
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    return await objects.update(id=id, o=o)


@router.delete("/")
async def delete_object(id: int,
                        objects: ObjectRepository = Depends(get_object_repository)):
    object = await objects.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    if object is None:
        raise not_found_exception
    await objects.delete(id=id)
    return {"status": True}
