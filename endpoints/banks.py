from fastapi import APIRouter

from parser_calc import get_banks

router = APIRouter()


@router.get("/")
async def read_banks(
        limit: int = 20,
        placements_value: int = 2000000,
        offset: int = 0,
        month: int = 18,
        initial_amount: int = 500000):
    data = get_banks(limit, placements_value,
                     offset, month, initial_amount)
    return data
