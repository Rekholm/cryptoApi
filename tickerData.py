import json


class tickerData():
    """
    Returns desired ticker information

    Usage: tickerData.openingPrice()

    Available functions:
    ask, bid, lastTradeClosed, volume, volumeWeightedAveragePrice, numberOfTrades,
    low, high, openingPrice
    """

    def __init__(self, listData, ticker):
        self.ticker = ticker
        self.listData = listData

    def returnAllData(self):
        print(f"""
                DATA FOR TICKER {self.ticker}

                {json.dumps(list(self.listData), indent=2)}
            """)

        return self.listData

    def ask(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(f"Current ASK price {self.listData[0]['Ask'][0]}")
        print(f"Whole lot volume {self.listData[0]['Ask'][1]}")
        print(f"Lot volume {self.listData[0]['Ask'][1]} \n")
        print("--------------")
        return self.listData[0]['Ask']

    def bid(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(f"Current BID price {self.listData[1]['Bid'][0]}")
        print(f"Whole lot volume {self.listData[1]['Bid'][1]}")
        print(f"Lot volume {self.listData[1]['Bid'][2]} \n")
        print("--------------")
        return self.listData[1]['Bid']

    def lastTradeClosed(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(f"Last trade closed: {self.listData[2]['Last trade closed'][0]}")
        print(
            f"Last trade lot volume {self.listData[2]['Last trade closed'][1]}")
        print("--------------")
        return self.listData[2]['Last trade closed']

    def volume(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(f"Volume today: {self.listData[3]['Volume'][0]}")
        print(f"Volume 24H: {self.listData[3]['Volume'][1]}")
        print("--------------")
        return self.listData[3]['Volume']

    def volumeWeightedAveragePrice(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(
            f"Weighted average price today: {self.listData[4]['Volume weighted average price'][0]}")
        print(
            f"Wighted average price 24H: {self.listData[4]['Volume weighted average price'][1]}")
        print("--------------")
        return self.listData[4]['Volume weighted average price']

    def numberOfTrades(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(
            f"Number of trades today: {self.listData[5]['Number of trades'][0]}")
        print(
            f"Number of trades 24H: {self.listData[5]['Number of trades'][1]}")
        print("--------------")
        return self.listData[5]['Number of trades']

    def low(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(f"Lowest price today: {self.listData[6]['Low'][0]}")
        print(f"Lowest price 24H: {self.listData[6]['Low'][1]}")
        print("--------------")
        return self.listData[6]['Low']

    def high(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(f"Highest price today: {self.listData[7]['High'][0]}")
        print(f"Highest price 24H: {self.listData[7]['High'][1]}")
        print("--------------")
        return self.listData[7]['High']

    def openingPrice(self):
        print("--------------")
        print(f"\nTICKER -- {self.ticker}")
        print(
            f"Opening price today {self.listData[8]['Todays opening price']}")
        return self.listData[8]['Todays opening price']
