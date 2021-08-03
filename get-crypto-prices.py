from logging import error
from time import time
from win10toast import ToastNotifier
import os
from binance import Client
import time

try:
    api_key = os.environ.get('binance_api')
    api_secret = os.environ.get('binance_secret')
    client = Client(api_key, api_secret)
    client.API_URL = 'https://api.binance.com/api'

    while range(10):
        coins = {}
        prices = ''

        coins['BTC'] = client.get_symbol_ticker(symbol="BTCUSDT")['price']
        coins['EOS'] = client.get_symbol_ticker(symbol="EOSUSDT")['price']
        coins['XTZ'] = client.get_symbol_ticker(symbol="XTZUSDT")['price']
        coins['ETH'] = client.get_symbol_ticker(symbol="ETHUSDT")['price']
        coins['ADA'] = client.get_symbol_ticker(symbol="ADAUSDT")['price']
        
        for coin in coins:
            prices += coin + '{0:.3}'.format(coins[coin]) 
            prices += '\n'

        toast = ToastNotifier() 
        toast.show_toast("Your prices:", prices)
        
        time.sleep(5 * 60)
except Exception as ex:
    raise ex

