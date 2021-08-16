from time import sleep
from binance import Client
from json import load
from gc import collect
from locale import setlocale, LC_ALL, currency
from toasts import toast

try:
    client = Client()
    client.API_URL = 'https://api.binance.com/api'

    def chunks(L, n):
        return [L[x : x + n] for x in range(0, len(L), n)]

    with open('coins.json') as json:
        coins = load(json)
        json.close()
        coins2 = chunks(coins, 4)

    for index in range(100):
        prices = ''
        setlocale(LC_ALL, 'en_US.UTF-8')

        for coingroup in coins2:
            for coins[0], coins[1] in coingroup:
                symbol = coins[1]
                prices += f'{coins[0]}: ' + currency(
                    float(client.get_symbol_ticker(symbol=f'{symbol}USDT')['price'])
                )
                prices += '\n'

            toast('Your coins: \n', prices)
            prices = ''

        del prices
        collect()

        sleep(10 * 60)
except Exception as ex:
    print(f'Erro: {ex}')
