#2: Use the binary search functions given in the text (recursive and iterative). 
# Generate a random, ordered list of integers and do a benchmark analysis for each one. What are your results? Can you explain them?

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


def binarySearchTraditional(alist, item):
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

def binarySearchRecursive(alist,item):
    """Does a binary search recursively"""
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearchRecursive(alist[:midpoint],item)
            else:
                return binarySearchRecursive(alist[midpoint+1:],item)

@time_decorator 
def testBinarySearchTraditional(li):
    """Tests binary search"""
    binarySearchTraditional(li,random.randint(1,len(li)))
    return len(li)

@time_decorator
def testBinarySearchRecursive(li):
    """Tests sequential search"""
    binarySearchRecursive(li,random.randint(1,len(li)))
    return len(li)

class testList(unittest.TestCase):
    """Tests the binarytraditional and binaryrecursive algorithms and acts as a main driver"""
    def testUnorderedList(self):
        """Compares binary and sequential searches on an ordered list of random integers."""
        print(testBinarySearchTraditional(sortedRandomList(100,1,100)))
        print(testBinarySearchTraditional(sortedRandomList(1000,1,1000)))
        print(testBinarySearchTraditional(sortedRandomList(10000,1,10000)))
        print(testBinarySearchTraditional(sortedRandomList(100000,1,100000)))
        print(testBinarySearchTraditional(sortedRandomList(1000000,1,100000)))

        print(testBinarySearchRecursive(sortedRandomList(100,1,100)))
        print(testBinarySearchRecursive(sortedRandomList(1000,1,1000)))
        print(testBinarySearchRecursive(sortedRandomList(10000,1,10000)))
        print(testBinarySearchRecursive(sortedRandomList(100000,1,100000)))
        print(testBinarySearchRecursive(sortedRandomList(1000000,1,1000000)))

if __name__ == '__main__':
    unittest.main()

#Results: it seems like the recursive solution is more wasteful. This makes sense, as opening multiple stack frames not only consumes memory but also takes a while compared to just handling the search in one function block.