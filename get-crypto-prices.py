from time import sleep
from win10toast import ToastNotifier
from os import environ
from binance import Client
import json
import gc

try:
    api_key = environ.get('binance_api')
    api_secret = environ.get('binance_secret')
    client = Client(api_key, api_secret)
    client.API_URL = 'https://api.binance.com/api'

    with open("get-crypto-prices\coins.json") as coins:
        json = json.load(coins)
        coins.close()

    for range in range(100):
        prices = ''
                
        for coin in json:
            prices += f'{coin}: ' + client.get_symbol_ticker(symbol=f'{json[coin]}USDT')['price'][:8]
            prices += "\n"

        toast = ToastNotifier() 
        toast.show_toast("Your prices:", prices)
        
        del prices
        gc.collect()

        sleep(5 * 60)
except Exception as ex:
    print(f'Erro: {ex}')

