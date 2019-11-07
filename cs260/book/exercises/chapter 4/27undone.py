# 27: The linked list implementation given above is called a singly linked list because each node has a single reference to the next node in sequence. An alternative implementation is known as a doubly linked list. In this implementation, each node has a reference to the next node (commonly called next) as well as a reference to the preceding node (commonly called back). The head reference also contains two references, one to the first node in the linked list and one to the last. Code this implementation in Python.

class Node:
    """Holds data for the UnorderedList class."""

    def __init__(self, initdata):
        """Initializes the class with data."""
        self.data = initdata
        self.next = None
        self.back = None

    def getData(self):
        """Returns data held within Node."""
        return self.data

    def getNext(self):
        """Gets the item that the Node is pointing at."""
        return self.next
    
    def getBack(self):
        """Gets the preceding Node."""
        return self.back

    def setBack(self, newdata):
        """Gets the preceding Node."""
        self.back = newdata

    def setData(self, newdata):
        """Replaces data held inside of Node."""
        self.data = newdata

    def setNext(self, newnext):
        """Sets what the Node is pointing at."""
        self.next = newnext

class Head:
    """Implements the Head class"""
    def __init__ (self):
        """Initializes Head ;)"""
        self.start = None
        self.end = None

    def getStart(self):
        """"Gets start"""
        return self.start

    def getEnd(self):
        """Gets end"""
        return self.end
    
    def setStart(self,newnode):
        """Sets start"""
        self.start = newnode

    def setEnd(self,newnode):
        """Sets end"""
        self.end = newnode

class DoublyLinkedList:
    """Implements the DoublyLinkedList data type"""

    def __init__(self):
        """Initializes an unordered list"""
        self.head = Head()
        self._size = 0

    def isEmpty(self):
        """Returns true if list is empty"""
        return self.head.getStart() == None

    def add(self, item):
        """Adds to the list"""
        self._size = self._size + 1
        temp = Node(item)
        temp.setNext(self.head.getStart())
        temp.setBack(self.head)
        self.head.setStart(temp)
        self.head.setEnd(temp)

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
        current = self.head.getStart()
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
            end = self.head.getEnd()
            secondtoend = end.getBack()
            secondtoend.setNext(None)
            return end
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

d = DoublyLinkedList()
d.add(1)
d.add(2)
d.add(3)
print(d)
print(d.size())
d.pop()
print(d)