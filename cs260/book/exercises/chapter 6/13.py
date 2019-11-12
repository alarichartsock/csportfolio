#13: Perform a benchmark analysis for a shell sort, using different increment sets on the same list.

import unittest
import time
import random

def randomList():
    """Creates a random list"""
    li = []
    for i in range(10000):
        li.append(random.randint(1, 100))
    return li

def shellSort(increments):
    """Algorithm for shell sort"""
    alist = randomList()
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

    #   print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // increments
    
    return alist

def gapInsertionSort(alist,start,gap):
    """Algorithm for gapInsertionSort"""
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def time_decorator(fn):
    """Sets up basic timekeeping"""
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

@time_decorator
def testShellSort(i):
    """Tests and times shell sorts at different increments."""
    shellSort(i)
    return i

class testInsertionSort(unittest.TestCase):
    """Tests to make sure that selection sort is working."""
    def testHashTable(self):
        """Acts as a main driver for the program, tests selection sort"""
        print(testShellSort(2))
        print(testShellSort(3))
        print(testShellSort(4))
        print(testShellSort(5))
        
if __name__ == '__main__':
    unittest.main()

#results:
# (2, 0.0827782154083252)
# (3, 0.06682324409484863)
# (4, 0.08676743507385254)
# (5, 0.21741676330566406)