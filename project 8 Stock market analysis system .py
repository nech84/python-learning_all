##project 8 Stock market analysis system 
#Dictionary Current stock data
stocks = {
    "AAPL":  {"price": 178, "sector": "Tech"},
    "GOOGL": {"price": 141, "sector": "Tech"},
    "TSLA":  {"price": 245, "sector": "EV"},
    "AMZN":  {"price": 185, "sector": "Retail"},
    "META":  {"price": 505, "sector": "Tech"},
    "NVDA":  {"price": 875, "sector": "Tech"},
    "MSFT":  {"price": 415, "sector": "Tech"},
    "NFLX":  {"price": 628, "sector": "Entertainment"},
}

#List Last 5 days price history
history = {
    "AAPL":  [165, 170, 172, 175, 178],
    "GOOGL": [130, 133, 138, 140, 141],
    "TSLA":  [280, 265, 250, 248, 245],
    "AMZN":  [175, 178, 180, 183, 185],
    "META":  [480, 488, 495, 500, 505],
    "NVDA":  [820, 835, 850, 865, 875],
    "MSFT":  [400, 405, 408, 412, 415],
    "NFLX":  [600, 610, 615, 620, 628],
}

class Stock:
    def __init__(self,name,price,sector,history):
        self.name = name
        self.price = price
        self.sector =  sector
        self.history  = history

    def average_price(self): #average price
        return sum(self.history) / len(self.history)
    
    def price_change_pct(self):
        return((self.history[-1] - self.history[0])/self.history[0])*100
    
    def  recommendation(self): 
        pct =  self.price_change_pct()
        if pct  > 5:
            return "STRONG BUY"
        elif pct >0:
            return "BUY"
        elif pct == 0:
            return "HOLD"
        else:
            return "sell"
        

stock_list =[
    Stock(name,stocks[name]["price"],stocks[name]["sector"],history[name])
    for  name in stocks
]

#loop analyze
for s in stock_list:
    print(f"{s.name} |  Avg {s.average_price():.2f}  |  Change:{s.price_change_pct():.2f}% | {s.recommendation()}")

#filter recommend stock
buy_list = list(filter(lambda s: s.recommendation() == "BUY",stock_list))

#map 
buy_name = list(map(lambda  s:s.name ,buy_list))

#methode
prices=list(map(lambda s: s.price,stock_list))
print(f"Average Price:{sum(prices)/len(prices):.2f}")
print(f"Highest: {max(prices)}")
print(f"Lowest:{min(prices)}")

sorted_stocks  =  sorted(stock_list,key=lambda s:s.price_change_pct(),reverse=True)
for i,s in enumerate(sorted_stocks,1):
    print(f"{i}.{s.name}|{s.price_change_pct():.2f}% |{s.recommendation()}")