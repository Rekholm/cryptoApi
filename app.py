import requests
import json



print("Enter the ticker for testing")
ticker = input().upper()

print("Choose currency EURO - 0 / USD - 1")
choice = input()
currency = ['EUR','USD']

#Kraken API
resp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={ticker}{currency[int(choice)]}')
data = resp.json()


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


def myfunk(elem):
    return {displayNames[elem]:keyData[elem]}

x = map(myfunk, list(keyData.keys()))



print(f"""
DATA FOR TICKER {ticker}

{json.dumps(list(x), indent=2)}
""")


print(data)