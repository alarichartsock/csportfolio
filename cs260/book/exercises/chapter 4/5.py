# 5: Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.

class Queue:
    """Traditional Queue implementation from runestone.academy."""
    def __init__(self):
        """Initializes Queue"""
        self.items = []

    def isEmpty(self):
        """Checks if the Queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Adds an item to the queue"""
        self.items.append(item)

    def dequeue(self):
        """Removes an item from the queue"""
        del self.items[0]
        return

    def size(self):
        """Returns total size of Queue"""
        return len(self.items)
    
    def show(self):
        """Prints the queue"""
        print(self.items)
        return

q = Queue()

import unittest

class test(unittest.TestCase):
    """Testing to make sure that the Queue is working as expected, LIFO, etc."""
    def testQueue(self):
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