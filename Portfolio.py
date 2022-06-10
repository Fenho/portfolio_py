from datetime import datetime

class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def profit(self, date_start, date_end):
        total = 0.0
        for stock in self.stocks:
            # for each stock, get the profit between the start and end dates
            stock_profit = self.cummulative_return(stock, date_start, date_end)
            total += self.annualized_return(stock_profit, date_start, date_end)
        return total

    @staticmethod
    def cummulative_return(stock, date_start, date_end):
        original_price = stock.price(date_start)
        final_price = stock.price(date_end)
        return (final_price - original_price) / original_price

    @staticmethod
    def annualized_return(stock_profit, date_start, date_end):
        days = (datetime.strptime(date_end, '%d-%m-%Y') - datetime.strptime(date_start, '%d-%m-%Y')).days
        annualized = ((1 + stock_profit / 100) ** (365 / days) - 1) * 100
        return annualized