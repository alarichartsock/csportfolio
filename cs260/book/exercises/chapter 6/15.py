# 15: One way to improve the quick sort is to use an insertion sort on lists that have a small length (call it the “partition limit”).
# Why does this make sense? Re-implement the quick sort and use it to sort a random list of integers. Perform an analysis using different list sizes for the partition limit.


import unittest
import random
import time

def quickSort(alist, limit):
    """Algorithm for quick sort"""
    if limit > len(alist):
        selectionSort(alist)
    else:
        quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   """Helps quick sort"""
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   """Partitions within the quick sort"""
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def selectionSort(alist):
   """Algorithm for a selection sort"""
   for fillslot in range(len(alist)-1, 0, -1):
       positionOfMax = 0
       for location in range(1, fillslot+1):
           if alist[location] > alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

def createList(O):
    """Creates a list of random integers."""
    li = []
    for i in range(O):
        li.append(random.randint(1,10000000000000000))
    return li

def time_decorator(fn):
    """Sets up basic timekeeping"""
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

@time_decorator
def testQuickSortTime(limit):
    """Tests quick sort's time"""
    quickSort(createList(15),limit)
    return limit

class testQuickSort(unittest.TestCase):
    """Tests to make sure that quick sort is working."""
    def testQuickSort(self):
        """Acts as a main driver for the program, tests quick sort"""
        s = [10,9,8,7,6,5,4,3,2,1]
        quickSort(s,3)
        self.assertEqual(s,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print(testQuickSortTime(14))
        print(testQuickSortTime(19))
        #My machine is too fast to test incremental time differences in small lists between quicksort and insertion sort.
        
if __name__ == '__main__':
    unittest.main()
