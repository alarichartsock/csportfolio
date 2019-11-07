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
    """Impletments the unorderedlist data type"""

    def __init__(self):
        """Initializes UnorderedList"""
        self.head = None
        self._size = 0

    def isEmpty(self):
        """Returns true if empty"""
        return self.head == None

    def add(self, item):
        """Adds item to UnorderedList"""
        self._size = self._size + 1
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """Returns unorderedList size"""
        return self._size

    def search(self, item):
        """Returns true is item is in list"""
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        """Removes an item from unordered List"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if found:
            self._size = self._size - 1


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
            self.assertEqual(myList.size(),6)


if __name__ == '__main__':
    unittest.main()

