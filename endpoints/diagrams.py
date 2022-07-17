import os

import matplotlib.pyplot as plt
from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def read_banks(numbers: str):
    numbers = list(numbers.split(', '))

    my_circle = plt.Circle((0, 0), 0.7, color='white')

    plt.pie(
        numbers,
        labels=numbers,
        textprops={'fontsize': 20},
        wedgeprops={'linewidth': 4, 'edgecolor': 'white'}
    )
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    plt.savefig(f"plot-{numbers}")

    path = os.path.dirname(os.path.abspath(__file__)) + f"\\plot-{numbers}"

    plt.show()
    return {"url": path}
