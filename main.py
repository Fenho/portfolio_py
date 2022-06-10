from Stock import Stock
from Portfolio import Portfolio
from faker import Faker
from random import random
import sys
import json

fake = Faker()
with open(sys.argv[1]) as json_file:
    data = json.load(json_file)

portfolios = []
for portfolio_j in data:
    portfolio = Portfolio(portfolio_j['name'])
    for stock_j in portfolio_j['stocks']:
        stock = Stock(stock_j['name'])
        for price_j in stock_j['prices']:
            stock.add_price(price_j['date'], price_j['price'])
        portfolio.add_stock(stock)
    portfolios.append(portfolio)

if __name__ == '__main__':
    date_start = sys.argv[2]
    date_end = sys.argv[3]
    print(portfolios[0].profit(date_start, date_end))
