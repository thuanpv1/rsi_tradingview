import pandas as pd
import requests
import json 
from rsi import rsi_tradingview

if __name__ == '__main__':
    response_API = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=201')
    data = response_API.text
    dataDetail = json.loads(data)
    for x in dataDetail:
        x[4] = float(x[4])
    mydf = pd.DataFrame(dataDetail,columns=['date', '1', '2', '3', 'close', '5', '6', '7', '8', '9', '10', '11'])

    rsi = rsi_tradingview(mydf, period=2)
    print("RSI: ")
    print(f"Date={mydf.index[200]}\tRSI={rsi[200]}")
