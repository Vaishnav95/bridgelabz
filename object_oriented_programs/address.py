"""Address Book
@Purpose: To create an address book to add, delete or update the info
@author: Vaishnav Goregaonkar
@date: 21/12/2019
"""

import json
import sys


class AddressBook:
    """This class contains methods for creating, updating and performing various operations on an address book
    """
    def __init__(self):
        self.data = {}

    def create_file(self):
        """This method creates a json file of an address book
        :return: created json file
        """
        self.data = {'data': []}
        file = input("Enter the file name to be created: ")
        with open(file + '.json', 'a+') as created:
            json.dump(self.data, created, indent=4)
            created.close()
            print("File successfully created!")

    def open_file(self):
        """This method opens an existing json file.
        :return: self.data
        """
        # file = input("Enter the file name to be opened: ")
        try:
            with open('Address.json', 'r') as new_file:
                self.data = json.load(new_file)
        except FileNotFoundError:
            print("Invalid File name!")

    def sort_zip_code(self):
        """This method sorts the address book according to the zip code of thr area
        :return: displays sorted address book
        """
        self.open_file()
        for i in range(len(self.data['data'])):
            for j in range(len(self.data['data'])):
                if self.data['data'][i]['zip_code'] < self.data['data'][j]['zip_code']:
                    self.data['data'][i], self.data['data'][j] = self.data['data'][j], self.data['data'][i]
        self.display()
        self.save()

    def sort_name(self):
        """This method sorts the address book according to the last name of the individual
        :return: sorted address book
        """
        self.open_file()
        for i in range(len(self.data['data'])):
            for j in range(len(self.data['data'])):
                if self.data['data'][i]['last_name'] < self.data['data'][j]['last_name']:
                    self.data['data'][i], self.data['data'][j] = self.data['data'][j], self.data['data'][i]
        self.display()
        self.save()

    def save(self):
        """This method saves the address book in the json format
        """
        file = input("Enter file name: ")
        with open(file + '.json', 'w+') as save_file:
            json.dump(self.data, save_file, indent=4)
            save_file.close()

    def address(self):
        """This method takes input from the user and creates an list of addresses
        :return: prints the address book
        """
        add_new = {}
        self.open_file()
        f_name = input("Enter First name: ")
        l_name = input("Enter last name: ")
        add = input("Enter Address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter zip code: ")
        phone_no = input("Enter phone number: ")

        if f_name.isalpha() and l_name.isalpha() and add.isalpha() and city.isalpha() and state.isalpha() \
                and zip_code.isnumeric() and phone_no.isnumeric():
            add_new['first_name'] = f_name
            add_new['last_name'] = l_name
            add_new['address'] = add
            add_new['city'] = city
            add_new['state'] = state
            add_new['zip_code'] = zip_code
            add_new['phone_no'] = phone_no

            self.data['data'].append(add_new)
            self.save()
            self.display()
            self.operation()
        else:
            print("Enter Correct values")
            self.address()

    def update(self):
        """This method helps the user to update his/her info except their first and last names
        :return: updated address
        """
        self.open_file()
        if len(self.data['data']) >= 1:
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            for i in range(len(self.data['data'])):
                if self.data['data'][i]['first_name'] == f_name \
                        and self.data['data'][i]['last_name'] == l_name:
                    flag = True
                    if flag:
                        print("Select anyone option to update your profile:")
                        choice = int(input("1 --> Address\n2 --> City\n3 --> State\n4 --> Zip Code\n5 --> Phone No.\n"
                                           "6 --> Quit\n"))
                        if choice == 1:
                            address = input("Enter updated address: ")
                            self.data['data'][i]['address'] = address
                            update = True
                            self.display()
                            self.save()
                        elif choice == 2:
                            city = input("Enter updated city: ")
                            self.data['data'][i]['city'] = city
                            update = True
                            self.display()
                            self.save()
                        elif choice == 3:
                            state = input("Enter updated state: ")
                            self.data['data'][i]['state'] = state
                            update = True
                            self.display()
                            self.save()
                        elif choice == 4:
                            zip_code = int(input("Enter updated zip code: "))
                            self.data['data'][i]['zip_code'] = zip_code
                            update = True
                            self.display()
                            self.save()
                        elif choice == 5:
                            phone_no = int(input("Enter updated phone number: "))
                            self.data['data'][i]['phone_no'] = phone_no
                            update = True
                            self.display()
                            self.save()
                        elif choice == 6:
                            pass
                        else:
                            print("Invalid")
                            update = False
                            self.operation()

    def display(self):
        """This method displays the addresses in the mailing label format
        """
        print(self.data)
        if len(self.data['data']) >= 1:
            print("First Name\t\t\t\tLast Name\t\t\t\tAddress\t\t\t\tCity\t\t\t\tState\t\t\t\tZip Code\t\t\t\t"
                  "Phone Number\n")
            try:
                for i in range(len(self.data['data'])):
                    print(self.data['data'][i]['first_name'], "\t\t\t\t", self.data['data'][i]['last_name'], "\t\t\t\t"
                          , self.data['data'][i]['address'], "\t\t\t\t", self.data['data'][i]['city'], "\t\t\t\t",
                          self.data['data'][i]['state'], "\t\t\t\t", self.data['data'][i]['zip_code'], "\t\t\t\t",
                          self.data['data'][i]['phone_no'], "\n")
            except ValueError:
                print("Invalid Key")

        else:
            print("No data found")
            again = input("Do you want to add a new record? y/n")
            if again.upper() == 'y' or again == 'yes' or again == 'Yes':
                self.address()
            else:
                sys.exit()

    def delete(self):
        """This method deletes the records in the address book
        """
        self.open_file()
        if len(self.data['data']) > 1:
            f_name = input("Enter First Name: ")
            l_name = input("Enter Last Name: ")
            for i in range(len(self.data['data'])):
                if str(self.data['data'][i]['first_name']).casefold() == f_name.casefold() \
                        and str(self.data['data'][i]['last_name']).casefold() == l_name.casefold():
                    del self.data['data'][i]
                    print("Data deleted successfully")
                    self.save()
                    self.display()
                    return
                else:
                    print("Data not found")

    def operation(self):
        """This method allows the user to perform required activities on the address book
        """
        print("1 --> Add an address\n"
              "2 --> Update an address\n"
              "3 --> Delete an address\n"
              "4 --> Print the list\n"
              "5 -- > Sort by name\n"
              "6 --> Sort by zip_code\n"
              "7 --> Create a file\n"
              "8 --> Exit")

        operate = int(input("Enter operation: "))

        if operate == 1:
            self.address()
        elif operate == 2:
            self.update()
        elif operate == 3:
            self.delete()
        elif operate == 4:
            self.display()
        elif operate == 5:
            self.sort_name()
        elif operate == 6:
            self.sort_zip_code()
        elif operate == 7:
            self.create_file()
        elif operate == 8:
            pass
        else:
            print("Wrong Input. Try Again!")
            self.operation()


def main():
    address_book = AddressBook()
    address_book.operation()


if __name__ == '__main__':
    main()
