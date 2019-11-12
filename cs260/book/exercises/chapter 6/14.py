#14: Implement the mergeSort function without using the slice operator.

import unittest

def mergeSort(alist):
    """Algorithm for a merge sort"""
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = []
        for q in range(mid):
            lefthalf.append(alist[q])
        righthalf = []
        for z in range(mid):
            righthalf.append(alist[mid + z])
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

class testInsertionSort(unittest.TestCase):
    """Tests to make sure that merge sort is working."""
    def testHashTable(self):
        """Acts as a main driver for the program, tests merge sort"""
        s = [10,9,8,7,6,5,4,3,2,1]
        mergeSort(s)
        self.assertEqual(s,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        
if __name__ == '__main__':
    unittest.main()
