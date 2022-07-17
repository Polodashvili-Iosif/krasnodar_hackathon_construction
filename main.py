from fastapi import FastAPI
from db.base import database
from endpoints import сonstruction_objects, banks, diagrams
import uvicorn

app = FastAPI(
    title="hackathon",
    description="API для хакатона",
    contact={
        "name": "Полодашвили Иосиф",
        "url": "https://t.me/Iosif_Polodashvili",
        "email": "iosif.polodashvili@mail.ru",
    },
    docs_url="/api/docs",
)

app.include_router(сonstruction_objects.router, prefix="/api/objects", tags=["objects"])
app.include_router(banks.router, prefix="/api/banks", tags=["banks"])
app.include_router(diagrams.router, prefix="/api/diagrams", tags=["diagrams"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
