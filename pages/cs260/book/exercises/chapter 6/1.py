#1: Set up a random experiment to test the difference between a sequential search and a binary search on a list of integers.

import random
import unittest
import time

def sortedRandomList(O,low,high):
    """Creates a list of random integers"""
    randomlist = []
    for i in range(O):
        randomnum = random.randint(low,high)
        randomlist.append(randomnum)
    randomlist.sort()
    return randomlist

def time_decorator(fn):
    """Sets up basic timekeeping"""
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

def orderedSequentialSearch(alist, item):
    """Algorithm for a sequential search on an ordered list"""
	    pos = 0
	    found = False
	    stop = False
	    while pos < len(alist) and not found and not stop:
	        if alist[pos] == item:
	            found = True
	        else:
	            if alist[pos] > item:
	                stop = True
	            else:
	                pos = pos+1
	
	    return found

def binarySearch(alist, item):
    """Algorithm for a binary search on an ordered list"""
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found

@time_decorator 
def testBinarySearch(li):
    """Tests binary search"""
    binarySearch(li,random.randint(1,len(li)))
    return len(li)

@time_decorator
def testSequentialSearch(li):
    """Tests sequential search"""
    orderedSequentialSearch(li,random.randint(1,len(li)))
    return len(li)

class testList(unittest.TestCase):
    """Tests the binary and sequential algorithms and acts as a main driver"""
    def testUnorderedList(self):
        """Compares binary and sequential searches on an ordered list of random integers."""
        print(testBinarySearch(sortedRandomList(100,1,100)))
        print(testBinarySearch(sortedRandomList(1000,1,1000)))
        print(testBinarySearch(sortedRandomList(10000,1,10000)))
        print(testBinarySearch(sortedRandomList(100000,1,100000)))
        print(testBinarySearch(sortedRandomList(1000000,1,100000)))

        print(testSequentialSearch(sortedRandomList(100,1,100)))
        print(testSequentialSearch(sortedRandomList(1000,1,1000)))
        print(testSequentialSearch(sortedRandomList(10000,1,10000)))
        print(testSequentialSearch(sortedRandomList(100000,1,100000)))
        print(testSequentialSearch(sortedRandomList(1000000,1,1000000)))

if __name__ == '__main__':
    unittest.main()

