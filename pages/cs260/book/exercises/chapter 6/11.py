# 11: A bubble sort can be modified to “bubble” in both directions. The first pass moves “up” the list, and the second pass moves “down.” 
# This alternating pattern continues until no more passes are necessary. 
# Implement this variation and describe under what circumstances it might be appropriate.

import unittest

def bubbleSort(a): 
    """Implements bubble sort with simultaineous selection, and a double pass."""
    n = len(a) 
    swapped = True
    start = 0
    end = n-1
    while (swapped==True): 
        swapped = False
  
        #bubbling up
        for i in range (start, end): 
            if (a[i] > a[i+1]) : 
                a[i], a[i+1]= a[i+1], a[i] 
                swapped=True
  
        #if nothing moved, then the array is already sorted baby
        if (swapped==False): 
            break
  
        swapped = False

        #item at end is at its rightful spot
        end = end-1
  
        #bubbling down
        for i in range(end-1, start-1,-1): 
            if (a[i] > a[i+1]): 
                a[i], a[i+1] = a[i+1], a[i] 
                swapped = True

        #increase starting point, the item at the beginning is in the right place
        start = start+1

class testBubbleSort(unittest.TestCase):
    """Tests to make sure that bubble sort is working."""
    def testHashTable(self):
        """Acts as a main driver for the program, tests bubble sort"""
        s = [10,9,8,7,6,5,4,3,2,1]
        bubbleSort(s)
        self.assertEqual(s,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
if __name__ == '__main__':
    unittest.main()

