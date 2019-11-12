# 10: Implement the bubble sort using simultaneous assignment.

import unittest

def bubbleSort(alist):
    """Algorithm for bubble sort, with simultaineous assignment"""
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1]= alist[i+1], alist[i] 

class testBubbleSort(unittest.TestCase):
    """Tests to make sure that bubble sort is working."""
    def testHashTable(self):
        """Acts as a main driver for the program, tests bubble sort"""
        s = [10,9,8,7,6,5,4,3,2,1]
        bubbleSort(s)
        self.assertEqual(s,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
if __name__ == '__main__':
    unittest.main()
