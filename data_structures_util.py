"""
This is a Util  class for data structures which contains all the functions performing the mentioned tasks.
Author: Vaishnav Goregaonkar
Date: 17/12/2019
"""


class Node:
    """Creating a Node class with reference initially set to None
    Parameters:
        data = the value contained in the node
    """

    def __init__(self, data):
        self.data = data
        self.ref = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.ref

    def set_next(self, new_next):
        self.ref = new_next


class LinkedList:
    """This is the class for the Linked List
    This class contains various methods that can be performed on the linked list
    The value of the start_node will be set to None since the Linked list will be empty at the time of creation
    """
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        """This function helps to traverse a linked list to read the data
        Returns:
            Displays the linked list elements
        """
        if self.start_node is None:  # Check whether the linked list is empty or not
            print("List has no element")
            return
        else:
            n = self.start_node  # Initialize a variable n with a a start variable
            while n is not None:
                print(n.data, " ")
                n = n.ref  # Print the data of the current node and set the value of n variable to n.ref

    def insert_at_start(self, data):
        """This function helps to insert an item at the start of the list
        Parameters:
            data: the item to be added at the start of the list
        """
        new_node = Node(data)  # Creating an object of the Node class
        new_node.ref = self.start_node  # Setting the reference to the start node
        self.start_node = new_node  # Setting the new object as the start node

    def insert_at_end(self, data):
        """This function inserts an item at the end of the list
        Parameters:
            data: The item to be added at the end of the list
        """
        new_node = Node(data)
        if self.start_node is None:  # Checking whether the linked list is empty or not
            self.start_node = new_node  # set the value of the start_node variable to the new_node object
            return
        n = self.start_node
        while n.ref is not None:  # Looping until we reach the last node
            n = n.ref
        n.ref = new_node  # Setting the reference of the last node to the new_node

    def insert_after_item(self, x, data):
        """This function adds data after another item
        Parameters:
            x: The item after which the new data has to be added
            data: The item to be added in the list
        """
        n = self.start_node
        while n is not None:  # Iterating through the loop to find the existing value
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Item is not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        """This function adds data before another item
        Parameters:
            x: The item before which the new data has to be added
            data: The item to be added in the list
        """
        if self.start_node is None:  # Checking if the list is empty or not
            print("List has no element")
            return

        if x == self.start_node.data:  # If the value before which the data has to be added is the first node
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Value not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):
        """The following function counts the number of elements in the list
        """
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count += 1
            n = n.ref
        return count

    def search_item(self, data):
        """This function traverses through the list to find the element
        Parameters:
            data: The value to be found
        Returns:
            returns True if found and False if not
        """
        if self.start_node is None:
            print("List is empty")
            return
        n = self.start_node
        while n is not None:
            if n.data == data:
                print("Item Found")
                return True
            n = n.ref
        print("Item not found")
        return False

    def delete_element(self, data):
        """This function deletes the value taken from the input
        Parameters:
            data: the value to be deleted
        """
        if self.start_node is None:
            print("List has no item to be deleted")
            return
        if self.start_node == data:  # Deleting the first node
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.data == data:  # Checking if the value of the node is equal to the value to be deleted
                break
            n = n.ref
        if n.ref is None:
            print("Item not found in the list")
        else:
            # Setting the ref of the previous node to the node which exists after the node which is being deleted
            n.ref = n.ref.ref

    def f_display(self):
        """This function adds the word to the string
        """
        current = self.start_node
        temp = ""
        while current:
            # print(current.data, end = ' ')
            temp = temp + current.data + " "
            current = current.get_next()
        return temp

    def bubble_sort(self):
        """This function sorts the list in an ascending order using bubble sort method
        """
        end = None
        while end != self.start_node:
            x = self.start_node
            while x.ref != end:
                y = x.ref
                if int(x.data) > int(y.data):
                    x.data, y.data = int(y.data), int(x.data)
                x = x.ref
            end = x


class Stack:
    """The following class creates an empty stack and performs various methods mentioned below
    """

    def __init__(self):
        self.items = []

    def push(self, element):
        """It adds the item to the top of the stack
        Parameters:
            element: The value to be added to the stack
        """
        self.items.append(element)

    def pop(self):
        """This function removes the top item from the stack and the stack is modified
        It needs no parameters
        Returns:
            The item that is removed
        """
        return self.items.pop()

    def is_empty(self):
        """This function checks whether the stack is empty or not
        Returns True if empty or else False
        """
        return self.items == []

    def top(self):
        """This function returns the top item of the stack
        """
        return self.items[-1]

    def get_stack(self):
        """This fun function returns all the items of the stack
        """
        return self.items

    def get_size(self):
        """This function returns the number of items in the stack
        """
        return len(self.items)

    def paren_balance(self, expression):
        """This function takes an arithmetic expression  and checks whether the expression is balanced or not using stack
        Parameters:
            expression: an arithmetic expression taken from an user input
        Returns:
            Check Whether the expression is balanced or not
        """

        open_paren = "({["  # A variable containing only the open parenthesis
        closed_paren = ")}]"  # A variable containing only the closed parenthesis

        for bracket in expression:
            if bracket in open_paren:  # Pushing the bracket if it is a Open parenthesis
                self.push(bracket)
            elif bracket in closed_paren:
                if self.is_empty():  # Checking if the stack is empty
                    balanced = False
                    break
                self.pop()  # Removing the bracket if it is a Closed parenthesis
        else:
            if self.is_empty():  # Returning True if stack is empty i.e. balanced
                balanced = True
            else:
                balanced = False  # Returning False if the stack is not empty i.e. unbalanced
        if balanced:
            print("Expression '", expression, "' is Balanced")
        else:
            print("Expression '", expression, "' is not Balanced")


class Queue:
    """This class stores items in a First In First Out manner.
    the following class creates and empty queue and performs the following methods
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """This method adds an item to the end of the queue
        Parameters:
            item: The value to be added to the queue
        """
        self.items.append(item)

    def dequeue(self):
        """This method removes the item at the beginning of the queue
        Returns:
            The item that is removed
        """
        if len(self.items) < 1:
            return None
        return self.items.pop(0)

    def is_empty(self):
        """This method checks whether the queue is empty or not
        """
        return self.items == []

    def get_size(self):
        """This method returns the number of items in the queue
        """
        return len(self.items)

    def get_queue(self):
        """This method prints the items in the queue
        """
        for item in self.items:
            print(item, )

    def cash_counter(self):
        """This is a function where people come to deposit cash or withdraw cash
        Input: Asking individuals to deposit or withdraw the amount
        """

        cash = 10000  # Initiating a variable which consists of the amount the bank has
        deposit = 0
        withdraw = 0

        while True:
            print("1 --> Deposit Cash")
            print("2 --> Withdraw Cash")
            print("3 --> Exit")
            # Taking user inputs for the type of transaction
            choice = int(input("Please enter a value: "))
            # If the user wants to deposit the cash
            if choice == 1:
                self.enqueue(1)
                # Amount to be deposited
                amount = int(input("Enter the amount to be desposited: "))
                if amount == 0:
                    print("Enter Amount!")
                else:
                    deposit += amount
                    cash += amount  # Adding the deposit to the total cash
                    print("Thank You!\nCash Deposited Successfully\n")
                self.dequeue()
            # If the user wants to withdraw cash
            elif choice == 2:
                withdraw += 1
                self.enqueue(1)

                amount = int(input("Enter the amount to withdraw: "))

                if cash >= amount:  # Checking if the amount to be withdrawed is available or not
                    deposit -= amount
                    cash -= amount  # Subtracting the withdrawal amount from the total cash
                    print("Thank You!\nCash Withdrawal Successful\n")
                else:
                    # If the withdrawal amount is more than the cash available
                    print("Insufficient Balance!\n")
                    self.dequeue()
            # If the user wants to exit
            elif choice == 3:
                quit()

            else:
                self.cash_counter()


class Deque:
    """This class stores the characters of the string and performs various methods
    """

    def __init__(self):
        self.deque = []

    def add_front(self, item):
        """This function adds the item to the left of the deque
        Parameters:
            item: The value to be added to the deque
        Returns a modified deque
        """
        self.deque.insert(0, item)

    def add_rear(self, item):
        """This function adds an item to the right of the deque
        Parameters:
              item: The value to be added
        Returns a modified deque
        """
        self.deque.append(item)

    def remove_front(self):
        """This function removes an item from the left of the deque
        Returns:
              The deleted value
        """
        return self.deque.pop(0)

    def remove_rear(self):
        """This function removes an item from the right side of the deque
        Returns:
              The removed value
        """
        return self.deque.pop()

    def is_empty(self):
        """This method checks whether the deque is empty or not
        """
        return self.deque == []

    def get_size(self):
        """This method returns the number of items in the deque
        """
        return len(self.deque)

    def get_deque(self):
        """This method prints the items of the deque
        """
        for item in self.deque:
            print(item, )

    def palindrome_checker(self, input_string):
        """This function is a check on a string for palindrome
        Parameters:
              input_string: The string as user input
        Returns:
              True if Palindrome and False if not
        """
        input_string = input_string.lower()
        for character in input_string:
            self.add_rear(character)

        if self.deque == self.deque[::-1]:  # Comparing the list with its reversed list
            print("{} is a Palindrome".format(input_string))
        else:
            print("{} is not a Palindrome".format(input_string))


class BinarySearchTree:
    """Number of Binary search trees
    This class contains methods which can perform the below mentioned methods
    """
    def __init__(self):
        pass

    def factorial(self, n):
        """This method calculates the factorial of a number
        Parameters:
              n: The integer input
        Returns:
              factorial: the calculated factorial of the number n
        """
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

    def catalan_formula(self, nodes):
        """This method uses the catalan formula to find out the number of binary search trees
        Parameters:
            nodes: Number of nodes of the binary search tree
        Returns:
             Returns the number of binary search trees that can be created using these many nodes
        """
        binary_search_tree_numbers = int(self.factorial(nodes*2)/(self.factorial(nodes+1) * self.factorial(nodes)))
        return binary_search_tree_numbers

    def binary_search_tree(self):
        """This method takes in a number of test cases and prints of the number of binary search trees for the
        respective number of nodes
        """
        test_cases = int(input("Enter a number of test cases: "))
        for i in range(test_cases):
            nodes_input = int(input("Enter the number of nodes: "))
            print("{} nodes : {} binary search trees".format(nodes_input, self.catalan_formula(nodes_input)))


class PrimeNumbers:
    """The following class contains methods to print out prime numbers range in each row in a 2D array
    """

    def __init__(self):
        pass

    def prime_number(self, low, high):
        """Prime numbers in a given range
        Parameters:
            low: lower value of that range
            high: upper value of the range
        Returns:
            A list of prime numbers in that range
        """
        prime_list = []
        # Traversing though the range
        for num in range(low, high + 1):
            # Checking if every number is divisible by their previous all the numbers
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    prime_list.append(num)
        return prime_list

    def prime_range(self, low, high):
        """This function prints the numbers in ranges of 100 in each row
        Parameters:
            low: lower value of that range
            high: upper value of the range
        Returns:
            A 2D array of prime numbers
        """
        new_array = []
        for i in range(low, high, 100):
            prime_num = self.prime_number(i, i+100)
            new_array.append(prime_num)
        return self.prime_printing(new_array, low, high)

    def prime_printing(self, new_array, low, high):
        """This function prints the individual elements of the array
        Parameters:
            new_array: an empty array created in the previous method
            low: lower value of that range
            high: upper value of the range
        Returns:
            prints elements of the array
        """
        i = 0
        for j in range(low, high, 100):
            # print("Range {} to {}".format(j, j+100))
            print(new_array[i])
            i += 1




