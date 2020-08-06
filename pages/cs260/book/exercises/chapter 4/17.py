# 17: Implement __str__ method so that lists are displayed the Python way (with square brackets).

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
        """Returns a stringified representation of the state of the list"""
        current = self.head
        strs = "[ "
        while current != None:
            strs = strs + str(current.getData()) +  ", "
            current = current.getNext()
        strs = strs + "]"
        return strs


class testList(unittest.TestCase):
    def testUnorderedList(self):
        """Tests unordered list data structure"""

        def setUp(self):
            myList = UnorderedList()
            mylist.add(31)
            mylist.add(77)
            mylist.add(17)
            mylist.add(93)
            mylist.add(26)
            mylist.add(54)
            self.assertEqual(myList.size(), 6)
            mylist.remove(93)
            self.assertEqual(myList.size(), 5)
            myList.add(31)
            self.assertEqual(myList.size(), 6)
            print(myList)

if __name__ == '__main__':
    unittest.main()