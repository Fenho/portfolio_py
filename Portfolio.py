class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def profit(self, date_start, date_end):
        total = 0
        for stock in self.stocks:
            # print(f"Start: {stock.price(date_start)}")
            # print(f"End {stock.price(date_end)}")
            # for each stock, get the profit between the start and end dates
            stock_profit = stock.price(date_end) - stock.price(date_start)
            total += stock_profit
        return total