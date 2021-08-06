from time import sleep
from os import environ
from binance import Client
from json import load
from gc import collect
from locale import setlocale, LC_ALL, currency
from toasts import toast

try:
    api_key = environ.get('binance_api')
    api_secret = environ.get('binance_secret')
    client = Client(api_key, api_secret)
    client.API_URL = 'https://api.binance.com/api'

    with open("get-crypto-prices\\coins.json") as coins:
        json = load(coins)
        coins.close()

    for index in range(100):
        prices = ''
        setlocale(LC_ALL, 'en_US')

        for coingroup in json:
            for coin in json[coingroup]:
                symbol = json[coingroup][coin]
                prices += f'{coin}: ' + currency(float(client.get_symbol_ticker(symbol=f'{symbol}USDT')['price']))
                prices += "\n"

            toast('Your coins: \n', prices)
            prices = ''

        del prices
        collect()

        sleep(5 * 60)
except Exception as ex:
    print(f'Erro: {ex}')
