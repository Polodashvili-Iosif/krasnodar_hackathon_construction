from pprint import pprint
from typing import Generator, Iterable, Mapping, Any, Optional

import requests


def get_banks(limit: int, placements_value: int, offset: int,
              month: int, initial_amount: int) -> Generator:
    headers = {
        'authority': 'public.sravni.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'Content-Type': 'application/json; charset=utf-8',
        'origin': 'https://www.sravni.ru',
        'pragma': 'no-cache',
        'referer': 'https://www.sravni.ru/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get(
        f'https://public.sravni.ru/v1/vitrins/products?productName=ipoteka&limit={limit}&offset={offset}&advertisingOnly=false&location=6.29.595.&&group=organization&groupLimit=5&sortProperty=advertising.position&sortDirection=asc&sum={placements_value}&term={month}&initialAmount={initial_amount}',
        headers=headers).json()

    banks = []
    for organization in response['organizations'].values():
        bank = {
            'Имя': organization['name']['short'],
            'Иконка': organization['logotypes']['square'],
            'Лицензия': f"Лиц. №{organization['license']}",
            'Рейтинг': f"{organization['ratingsInfo']['complexCalculatedRatingValue']:.1f}",
            'id': organization['id']
        }

        for item in response['items']:
            if item['organization'] == bank['id']:
                bank.update(
                    Программа=item['name'],
                    МинСтавка=item['minRate'],
                    EжемесПлатёж=int(item['payment']),
                    Переплата=int(item['overPayment']),
                )

                banks.append(bank)
    return banks


def main():
    banks = get_banks(20, 2000000, 0, 18, 500000)
    pprint(banks)


if __name__ == '__main__':
    main()
