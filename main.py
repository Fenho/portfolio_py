from Stock import Stock
from Portfolio import Portfolio
from faker import Faker
from random import random
import sys

fake = Faker()
for i in range(2):
    stock = Stock(fake.company())
    portfolio = Portfolio(fake.name())
    for i in range(10):
        stock = Stock(fake.company())
        for i in range(10):
            fake_date = fake.date_between(start_date='-30y', end_date='today').strftime('%d-%m-%Y')
            stock.add_price(fake_date,
                round(random() * 10000, 2))
        portfolio.add_stock(stock)

if __name__ == '__main__':
    date_start = sys.argv[1]
    date_end = sys.argv[2]
    print(portfolio.profit(date_start, date_end))
