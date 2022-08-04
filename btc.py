from numpy import number
import requests
import pandas as pd

def get_price(coin):
    bitcoin_api_url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}"
    response = requests.get(bitcoin_api_url)
    resp_json = response.json()
    return resp_json['price']

def get_all_sumbols():
    bitcoin_api_url = "https://api.binance.com/api/v1/exchangeInfo"
    response = requests.get(bitcoin_api_url)
    symbols = response.json()
    df = pd.DataFrame(symbols['symbols'])
    list_of_all_symbols = []
    for index, data in df.iterrows():
        if data['isSpotTradingAllowed'] == True:
            list_of_all_symbols.append(data['symbol'])

    return list_of_all_symbols
