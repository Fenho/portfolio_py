import unittest
from Stock import Stock
from Portfolio import Portfolio
import json

date_start1 = '01-01-2021'
date_end1 = '01-01-2022'

with open('examples/simple.json') as json_file:
    data = json.load(json_file)

examples = []
for portfolio_j in data:
    portfolio = Portfolio(portfolio_j['name'])
    for stock_j in portfolio_j['stocks']:
        stock = Stock(stock_j['name'])
        for price_j in stock_j['prices']:
            stock.add_price(price_j['date'], price_j['price'])
        portfolio.add_stock(stock)
    examples.append(portfolio)

date_start2 = '01-01-2018'
date_end2 = '01-01-2021'

with open('examples/set1.json') as json_file:
    data_set1 = json.load(json_file)

examples_set1 = []
for portfolio_j in data_set1:
    portfolio = Portfolio(portfolio_j['name'])
    for stock_j in portfolio_j['stocks']:
        stock = Stock(stock_j['name'])
        for price_j in stock_j['prices']:
            stock.add_price(price_j['date'], price_j['price'])
        portfolio.add_stock(stock)
    examples_set1.append(portfolio)

class TestPortfolio(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(round(examples[0].profit(date_start1, date_end1), 2), 2.54)

    def test_set1(self):
        self.assertEqual(round(examples_set1[0].profit(date_start2, date_end2), 2), 1.89)


if __name__ == '__main__':
    unittest.main()