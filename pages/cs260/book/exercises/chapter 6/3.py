# 3: Implement the binary search using recursion without the slice operator. 
# Recall that you will need to pass the list along with the starting and ending index values for the sublist. Generate a random, ordered list of integers and do a benchmark analysis.

import unittest

def binarySearchRecursive(alist, item,start,end):
    """Returns a binary search without using a slice operator for arrays"""
    if end-start <= 0:
        return False
    else:
        midpoint = (end-start)//2
    if alist[midpoint+1]==item:
        return True
    else:
        if item<alist[midpoint]:
            return binarySearchRecursive(alist,item,start,midpoint)
        else:
            return binarySearchRecursive(alist,item,midpoint+1,end)

class testList(unittest.TestCase):
    """Tests the binarySearchRecursive, acts as a main driver"""
    def testUnorderedList(self):
        """Compares binary and sequential searches on an ordered list of random integers."""
        l = [1,2,3,4,5,6,7,8,9,10]
        print(binarySearchRecursive(l,1,0,10))

if __name__ == '__main__':
    unittest.main()

