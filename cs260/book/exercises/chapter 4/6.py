#6: Design and implement an experiment to do benchmark comparisons of the two queue implementations. What can you learn from such an experiment?

import time

class NewQueue:
    """Modified Queue for decreased time complexity"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        del self.items[0]
        return

    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
        return

class Queue:
    """Traditional Queue implementation."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def time_decorator(fn):
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
    for i in range(O):
        print(TestOldQueueEnque(i*1000))

def testNewAccurately(O):
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