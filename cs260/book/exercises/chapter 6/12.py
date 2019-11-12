#12: Implement the selection sort using simultaneous assignment.

import unittest

def selectionSort(alist):
   """Algorithm for a selection sort with simultaineous assignment"""
   for fillslot in range(len(alist)-1, 0, -1):
       positionOfMax = 0
       for location in range(1, fillslot+1):
           if alist[location] > alist[positionOfMax]:
               positionOfMax = location

       alist[fillslot],alist[positionOfMax] = alist[positionOfMax],alist[fillslot]

class testSelectionSort(unittest.TestCase):
    """Tests to make sure that selection sort is working."""
    def testHashTable(self):
        """Acts as a main driver for the program, tests selection sort"""
        s = [10,9,8,7,6,5,4,3,2,1]
        selectionSort(s)
        self.assertEqual(s,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
if __name__ == '__main__':
    unittest.main()
