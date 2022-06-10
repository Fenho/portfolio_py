# Portfolio.py 🐍 for Fintual homework 📚
A Portfolio class that has a Profit method which takes two dates and returns the profit made between those.

## Classes 🦆
### Portfolio
Portfolio class with a name and a collection of Stocks. Has the profit method that calculates the sum of the annualized returns of all the stocks, between a given first date and older_date

### Stock
Stock class with a name and an OrderedDict (more info about this [here](https://www.geeksforgeeks.org/ordereddict-in-python/)) where the keys are dates and the values are the prices the stock had in that date 😵.

## Into the gist of it 🤠
To run the script you just have to run this in the console:
```
python3 main.py set date_start date_end
```
Where:
- set is a .json file where all the mock data is stored.
- date_start is just the oldest date, while date_end the newest, being both in 'day-mont-year' format.

Making fake data may be  ✨ annoying ✨  so there is another script called 'example_generator.py' that will generate fake data and store it in a json in the folder 'examples'.
To run 'example_generator.py' you have to run it like this:
```
python3 example_generator.py json_name portfolio_amount stock_amount price_amount
```
Where:
- json_name is the name of the file where the data will be stored (don't forget about the .json). the root folder for this is the 'examples' folder.
- portfolio_amount is the amount of portfolios you want to generate
- stock_amount is the same as before but with stocks
- price_amount is the amount of prices in different dates you want. The date is a random one between today and 30 years ago.

Testing data may also be  ✨ annoying ✨ (especially when you are developing and you break stuff that worked just fine minutes ago), so there is a testing script called 'test_portfolio.py'. You run it like this:
```
python3 test_portfolio.py
```
The first test uses the simple.json set of data, being the first date '01-01-2021', and the newest one '01-01-2022'. The portfolio tested just has 2 stocks, where each stock has 2 dates and prices.
The second test uses the set1.json set of data, being the first date '01-01-2018', and the newest one '01-01-2021'. The portfolio tested has 10 stocks, where each stock has 10 dates and prices.

### Notes 👀:
- Each price that is added to the profit is annualized.
- Depending on the data generated you may not be able to get a value for profit with certain dates (maybe you input a start date where the year is 2010, but the oldest year in the generated daya may be 2018).
- There is no GUI, just the console 😄
