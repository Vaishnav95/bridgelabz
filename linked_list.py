"""
"""


class Node:
    """Creating a Node class with reference initially set to None
    Parameters:
        data = the value contained in the node
    """
    def __init__(self, data):
        self.data = data
        self.ref = None


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
            if n.ref.item == data:  # Checking if the value of the node is equal to the value to be deleted
                break
            n = n.ref
        if n.ref is None:
            print("Item not found in the list")
        else:
            # Setting the ref of the previous node to the node which exists after the node which is being deleted
            n.ref = n.ref.ref

    def f_display(self):
        current = self.start_node
        temp = ""
        while current:
            # print(current.data, end = ' ')
            temp = temp + current.data + " "
            current = current.get_next()
        return temp
