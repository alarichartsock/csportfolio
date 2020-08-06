# 25: Design and implement an experiment that will compare the performance of a Python list with a list implemented as a linked list.

import time

def time_decorator(fn):
    """Sets up basic timekeeping"""
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

lst = []

@time_decorator
def TestPythonListAppend(O):
    """Testing the big O of the List Index method"""
    for i in range(O):
        lst.append(1)
    return O

print(TestPythonListAppend(1))
print(TestPythonListAppend(10))
print(TestPythonListAppend(100))
print(TestPythonListAppend(1000))
# print(TestPythonListAppend(10000))
# print(TestPythonListAppend(100000))
# print(TestPythonListAppend(1000000))
# print(TestPythonListAppend(10000000))
# print(TestPythonListAppend(100000000))
# print(TestPythonListAppend(1000000000))
# print(TestPythonListAppend(10000000000))
# print(TestPythonListAppend(100000000000))

class Node:
    """Holds data for the UnorderedList class."""

    def __init__(self, initdata):
        """Initializes the class with data."""
        self.data = initdata
        self.next = None

    def getData(self):
        """Returns data held within Node."""
        return self.data

    def getNext(self):
        """Gets the item that the Node is pointing at."""
        return self.next

    def setData(self, newdata):
        """Replaces data held inside of Node."""
        self.data = newdata

    def setNext(self, newnext):
        """Sets what the Node is pointing at."""
        self.next = newnext

class UnorderedList:
    """Implements the UnorderedList data type"""

    def __init__(self):
        """Initializes an unordered list"""
        self.head = None
        self._size = 0

    def isEmpty(self):
        """Returns true if list is empty"""
        return self.head == None

    def add(self, item):
        """Adds to the list"""
        self._size = self._size + 1
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """Returns size of list"""
        return self._size

    def search(self, item):
        """Searches the unordered list"""
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        """Removes an item from the list"""
        if(self.size == 0):
            pass
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if found != True:
                return
            else:
                self._size = self._size - 1
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def __str__(self):
        """Returns a stringified representation of the lists's state"""
        current = self.head
        strs = "[ "
        while current != None:
            strs = strs + str(current.getData()) + ", "
            current = current.getNext()
        strs = strs + "]"
        return strs

    def append(self, item):
        """Adds an item to the end of the list"""
        current = self.head
        if current == None:
            self.head = Node(item)
            return
        while current.getNext() != None:  # navigating to end of list
            current = current.getNext()
        current.setNext(Node(item))

    def index(self, i):
        """Returns the value of the index of something in the list"""
        ind = 0
        current = self.head
        while current != None and ind != i:
            current = current.getNext()
            ind = ind + 1
        return current.getData()

    def pop(self, index=None):
        """Removes and returns the last item of the list"""
        if index == None:
            current = self.head
            previous = None
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            return previous.getData()
        else:
            current = self.head
            previous = None
            i = 0
            while current != None and index != i:
                previous = current
                current = current.getNext()
                i = i + 1
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return current.getData()

    def insert(self, index, data):
        """Inserts an item at a specific index into the list"""
        current = self.head
        previous = None
        i = 0
        datanode = Node(data)
        while current != None and index != i:
            previous = current
            current = current.getNext()
            i = i + 1
        previous.setNext(datanode)
        datanode.setNext(current)

    def slice(self, start, stop):
        """Returns a copy of the list slice at those indexes"""
        current = self.head
        i = 0
        while current != None and start != i:  # navigating to start
            current = current.getNext()
            i = i + 1
        copyList = UnorderedList()
        while current != None and stop != i:
            copyList.add(current.getData())
            current = current.getNext()
            i = i + 1
        return copyList

ul = UnorderedList()

@time_decorator
def TestUnorderedListAppend(O):
    """Testing the big O of the List Index method"""
    for i in range(O):
        ul.append(1)
    return O

print(TestUnorderedListAppend(1))
print(TestUnorderedListAppend(10))
print(TestUnorderedListAppend(100))
print(TestUnorderedListAppend(1000))
# print(TestUnorderedListAppend(10000))
# print(TestUnorderedListAppend(100000))
# print(TestUnorderedListAppend(1000000))
# print(TestUnorderedListAppend(10000000))
# print(TestUnorderedListAppend(100000000))
# print(TestUnorderedListAppend(1000000000))
# print(TestUnorderedListAppend(10000000000))
# print(TestUnorderedListAppend(100000000000))
# print(TestUnorderedListAppend(1000000000000))
# print(TestUnorderedListAppend(10000000000000))

#Python lists looks to be O(1) and the unordered list looks to be O(n^2)