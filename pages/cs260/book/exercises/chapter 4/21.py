# 21: Consider the relationship between Unordered and Ordered lists. Is it possible that inheritance could be used to build a more efficient implementation? Implement this inheritance hierarchy.

# Yes, there could be an inheritance hierarchy that could make that more efficient.

import unittest


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

class UnorderedList():
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

class OrderedList(UnorderedList):
    """Ordered list implementation from runestone.academy"""

    def __init__(self):
        """Implements an ordered list"""
        self.head = None

    def search(self, item):
        """Searches the ordered list for item, returns true if true"""
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        """Adds an item to the ordered list"""
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        """Returns the size of the ordered list"""
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

class testList(unittest.TestCase):
    def testUnorderedList(self):
        """Tests unordered list data structure"""
        def setUp(self):
            myList = UnorderedList()
            myList.add(7)
            myList.add(17)
            myList.add(27)
            print(myList)
            myList.pop()
            myList.insert(2,20)
            myList.insert(2,10)
            myList.insert(2,10)
            myList.append(10)
            self.assertEqual(myList.slice(1,3), [ 10, 17, ])
            myList.pop(1)
            self.assertEqual(myList,[[ 27, 10, 10, 20, 10, ]])

if __name__ == '__main__':
    unittest.main()

