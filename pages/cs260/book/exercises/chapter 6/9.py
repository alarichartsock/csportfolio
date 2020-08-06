# 9: Using a random number generator, create a list of 500 integers.
# Perform a benchmark analysis using some of the sorting algorithms from this chapter. What is the difference in execution speed?

import random
import time
import unittest

def randomList():
    """Creates a random list"""
    li = []
    for i in range(500):
        li.append(random.randint(1, 100))
    return li

def time_decorator(fn):
    """Sets up basic timekeeping"""
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

def bubbleSort(alist):
    """Algorithm for bubble sort"""
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

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

def insertionSort(alist):
   """Algorithm for an insertion sort"""
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

@time_decorator
def testBubbleSort(l):
    """Tests the speed of bubble sort"""
    bubbleSort(randomList())
    return l

@time_decorator
def testSelectionSort(l):
    """Tests the speed of selection sort"""
    selectionSort(randomList())
    return l

@time_decorator
def testInsertionSort(l):
    """Tests the speed of the insertion sort"""
    insertionSort(randomList())
    return l

class testSorts(unittest.TestCase):
    """Tests the speed of the bubble, insertion, and selection sorts"""
    def testHashTable(self):
        """Acts as a main driver for the program"""
        print(testBubbleSort("bubblesort"))
        print(testInsertionSort("insertionsort"))
        print(testSelectionSort("selectionsort"))
        
if __name__ == '__main__':
    unittest.main()

# Results on my machine
# ('bubblesort', 0.03390836715698242)
# ('insertionsort', 0.017931222915649414)
# ('selectionsort', 0.014984607696533203)

#So as expected, bubble sort is much slower than the other two sorting algorithms, with selection sort having a hair faster performance than insertion sort.