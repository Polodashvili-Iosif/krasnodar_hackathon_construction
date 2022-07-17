from dotenv import dotenv_values
from psycopg2 import connect
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_banks(
        limit: int = 20,
        placements_value: int = 2000000,
        offset: int = 0,
        month: int = 18,
        initial_amount: int = 500000):
    config = dotenv_values(".env")
    with connect(host=config['HOST'],
                 user=config['POSTGRES_USER'],
                 password=config['POSTGRES_PASSWORD'],
                 database=config['POSTGRES_DB'],
                 port=config['PORT']) as connection:
        with connection.cursor() as cursor:
            for status in []:
                cursor.execute(
                    f"""SELECT COUNT(*) 
                     FROM placements
                     WHERE status={status};"""
                )
