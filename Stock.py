from datetime import datetime
from collections import OrderedDict

class Stock:
    def __init__(self, name):
        self.name = name
        self.prices = OrderedDict()
    
    def add_price(self, date, price):
        self.prices[date] = price
        self.prices = OrderedDict(sorted(self.prices.items(), key = lambda x: datetime.strptime(x[0], '%d-%m-%Y'), reverse=True))
    
    def price(self, date):
        # approximate date to the closest below if not found
        for key in self.prices:
            if datetime.strptime(key, '%d-%m-%Y') <= datetime.strptime(date, '%d-%m-%Y'):
                return self.prices[key]
        return "No hay precio para esa fecha (o antes)"