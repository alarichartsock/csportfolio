#6: Design and implement an experiment to do benchmark comparisons of the two queue implementations. What can you learn from such an experiment?

import time

class NewQueue:
    """Modified Queue for decreased time complexity"""
    def __init__(self):
        """Sets up queue"""
        self.items = []

    def isEmpty(self):
        """Returns true if the queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Puts an item in the queue"""
        self.items.append(item)

    def dequeue(self):
        """Removes an item from the queue"""
        del self.items[0]
        return

    def size(self):
        """Returns the size of the queue"""
        return len(self.items)
    
    def show(self):
        """Prints the queue"""
        print(self.items)
        return

class Queue:
    """Traditional Queue implementation."""
    def __init__(self):
        """Initializes a queue"""
        self.items = []

    def isEmpty(self):
        """Returns true if the queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Adds an item to the queue"""
        self.items.insert(0,item)

    def dequeue(self):
        """Removes an item from the queue"""
        return self.items.pop()

    def size(self):
        """Returns the size of the queue"""
        return len(self.items)

def time_decorator(fn):
    """Sets up basic timekeeping"""
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

#I'm going to test the big O of enqueue operations.

#Testing enqueue operations

@time_decorator
def TestOldQueueEnque(O):
    """Testing the big O of the List Index method"""
    old = OldQueue()
    for i in range(O):
        old.enqueue(i)
    return O

@time_decorator
def TestNewQueueEnque(O):
    """Testing the big O of the List Index method"""
    new = NewQueue()
    for i in range(O):
        new.enqueue(i)
    return O

def testOldAccurately(O):
    """Tests old queue accurately"""
    for i in range(O):
        print(TestOldQueueEnque(i*1000))

def testNewAccurately(O):
    """Tests new queue accurately"""
    for i in range(O):
        print(TestNewQueueEnque(i*1000))

#print(testOldAccurately(100000))
#Yep, definetly looks to be O(n^2)
print(testNewAccurately(100000))
#looks to be O(n)

#Looks to be 

import unittest

class test(unittest.TestCase):
    def testQueue(self):
        """Tests queue"""
        q = NewQueue()
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