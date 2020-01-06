"""Commercial Data Processing
@Purpose: Maintains tracks of shares purchased as well as datetime of transaction
@author: Vaishnav Goregaonkar
@date: 26/12/2019
"""

from datetime import datetime
import linked_list_stock


class Share:
    """This class is used by financial institution to keep track of customer information
    """

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.time_transact = time_transaction()


def time_transaction():
    """This method keeps track of the time of the transaction
    :return: current time
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


class StockAccount:
    """This class contains methods to buy or sell the shares"""
    def __init__(self):
        self.value = 0
        self.company_shares_list = linked_list_stock.LinkedList()
        self.stock_list = []

    def add_shares(self, name, number):
        """This method adds the shares to the existing company
        :param name: name of the company
        :param number: number of shared purchased
        :return: list of company and shares
        """
        new_share = Share(name, number)
        self.company_shares_list.add_to_list(new_share)
        self.stock_list.append(new_share)

    def buy(self, new_name, new_number):
        """This method buys shares for the existing company or adds the company if the company doesn't exist in the list
        :param new_name: name of the company
        :param new_number: number of shares
        :return: appends the shares to the company
        """
        flag = False
        for i in self.stock_list:  # If the name exists in the stock list
            if new_name == i.name:
                self.company_shares_list.delete_node(i)
                i.number += new_number
                flag = True
                i.time_transact = time_transaction()
                self.company_shares_list.add_to_list(i)

        if flag is False:
            new_share = Share(new_name, new_number)
            new_share.time_transact = time_transaction()
            self.stock_list.append(new_share)
            self.company_shares_list.add_to_list(new_share)

    def sell(self, sell_name, sell_number):
        """This method sells the stocks of the company and displays the remaining stocks
        :param sell_name: name of the company
        :param sell_number: number of shares
        :return: the remaining shares of that company
        """
        flag = False
        for i in self.stock_list:
            if sell_name == i.name:
                self.company_shares_list.delete_node(i)
                i.number -= sell_number
                i.time_transact = time_transaction()
                self.company_shares_list.add_to_list(i)
                if i.number == 0:
                    self.stock_list.remove(i)
                    self.company_shares_list.delete_node(i)
                flag = True
        if flag is False:
            print("\rNo such share available for sale!!!")

    def print_report(self):
        """This method displays the number of shares of the following company with the time of the purchase
        """
        for i in self.stock_list:
            print("\n{} shares of {} purchased at {}".format(i.number, i.name, i.time_transact))

    def save_file(self):
        """This method saves the report in the text format
        """
        file_object = open("./Inventory_data_final.txt", 'w')
        for i in self.stock_list:
            data = str("\n{} shares of {} purchased at {}".format(i.number, i.name, i.time_transact))
            file_object.write(data)


def main():
    jpm = StockAccount()
    jpm.add_shares("samsung", 220)
    jpm.add_shares("apple", 120)
    jpm.add_shares("oppo", 90)
    jpm.add_shares("nokia", 100)
    jpm.print_report()
    print("\n")
    jpm.buy('apple', 80)
    jpm.print_report()
    print("\n")
    jpm.sell("nokia", 50)
    jpm.print_report()
    jpm.save_file()


# driver function
if __name__ == "__main__":
    main()
