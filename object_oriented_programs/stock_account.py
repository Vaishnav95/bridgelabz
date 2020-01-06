"""Stock account management
@Purpose: Print a stock report with value of each stock
@author: Vaishnav Goregaonkar
@date: 27/12/2019
"""


class Share:
    """This class contains info about the stocks owned by an individual
    """

    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number


class Portfolio:
    """This class contains methods for creating a portfolio for stock account
    """

    def __init__(self):
        self.value = 0
        self.portfolio = []

    def enter_stock(self, name, price, number):
        """This method adds new account in the portfolio
        Parameters:
            name: name of the individual
            price: price of the stocks
            number: no. of shares purchased
        """
        new_stock = Share(name, price, number)
        self.portfolio.append(new_stock)

    def portfolio_details(self):
        """This method calculates the total value of the stocks
        """
        for i in self.portfolio:
            print("\r{}:\n\tPrice: {}\n\tNumber: {}\n\tValue: {}\n.".format(i.name, i.price, i.number,
                                                                            i.price * i.number))

    def portfolio_total(self):
        """This method iterates through the portfolio and calculates the stock value"""
        for i in self.portfolio:
            self.value += i.number * i.price


if __name__ == "__main__":
    port = Portfolio()
    port.enter_stock("Samsung", 35, 150)
    port.enter_stock("Apple", 45, 160)
    port.portfolio_details()
    port.portfolio_total()
    print("Total portfolio value = ", port.value)
