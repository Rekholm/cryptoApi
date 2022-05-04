import requests
from tickerData import tickerData


print("Enter the ticker for testing")
ticker = input().upper()

print("Choose currency EURO - 0 / USD - 1")
choice = input()
currency = ['EUR','USD']

#Kraken API
krakenResp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={ticker}{currency[int(choice)]}')
data = krakenResp.json()


keyData = data['result'][list(data['result'].keys())[0]]

displayNames = {'a': 'Ask',
                'b': 'Bid',
                'c': 'Last trade closed',
                'v': 'Volume',
                'p': 'Volume weighted average price',
                't': 'Number of trades',
                'l': 'Low',
                'h': 'High',
                'o': 'Todays opening price',
                }


# def zipper(elem):
#     return {displayNames[elem]:keyData[elem]}
# tickerData = map(zipper, list(keyData.keys()))

mapData = map(lambda elem: {displayNames[elem]:keyData[elem]}, list(keyData.keys()))
listData = list(mapData)




currentTickerData = tickerData(listData, ticker)

currentTickerData.high()
