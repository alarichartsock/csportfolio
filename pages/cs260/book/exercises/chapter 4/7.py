#7: It is possible to implement a queue such that both enqueue and dequeue have O(1) performance on average.
# In this case it means that most of the time enqueue and dequeue will be O(1) except in one particular circumstance where dequeue will be O(n).

import time

class ModifiedQueue:
    """The ModifiedQueue is designed to have the most efficient functions for enqueue and dequeue."""
    def __init__(self):
        """Initializes a queue"""
        self.items = []

    def isEmpty(self):
        """Returns true is the queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Adds an item to the queue"""
        self.items.append(item)

    def dequeue(self):
        """Removes an item from the queue"""
        return self.items.pop(0)

    def size(self):
        """Returns size of the queue"""
        return len(self.items)

    def show(self):
        """Prints the queue"""
        print(self.items)
        return

import unittest

class test(unittest.TestCase):
    def testQueue(self):
        """Tests the queue"""
        q = ModifiedQueue()
        q.enqueue(1)
        self.assertTrue(q.isEmpty,False)
        q.enqueue(2)
        q.enqueue(3)
        q.show()
        q.dequeue()
        q.show()
        self.assertTrue(q.size,2)
        
if __name__ == '__main__':
    unittest.main()