class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# A class to represent a queue

# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    # Method to add an item to the queue
    def en_queue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

        # Method to remove an item from queue

    def de_queue(self):

        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return str(temp.data)

    def print_list(self):
        if self.is_empty():
            return
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next


# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.en_queue(10)
    q.en_queue(20)
    q.de_queue()
    q.de_queue()
    q.en_queue(30)
    q.en_queue(40)
    q.en_queue(50)

    print("Dequeued item is " + q.de_queue())
    q.print_list()
