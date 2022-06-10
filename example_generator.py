from Stock import Stock
from Portfolio import Portfolio
from faker import Faker
from random import random
import json
import sys

fake = Faker()
example_data = []
for i in range(int(sys.argv[2])):
    portfolio = fake.name()
    portfolio_data = { 'name': portfolio }
    stocks = []
    for i in range(int(sys.argv[3])):
        stock = fake.company()
        prices = []
        for i in range(int(sys.argv[4])):
            fake_date = fake.date_between(start_date='-30y', end_date='today').strftime('%d-%m-%Y')
            fake_price = round(random() * 10000, 2)
            prices.append({ 'date': fake_date, 'price': fake_price })
        stocks.append({ 'name': stock, 'prices': prices })
    portfolio_data['stocks'] = stocks
    example_data.append(portfolio_data)

json_string = json.dumps(example_data)
with open(f"examples/{sys.argv[1]}", 'w') as outfile:
    outfile.write(json_string)