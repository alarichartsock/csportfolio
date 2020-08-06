# 6: Create a binary heap with a limited heap size. In other words, the heap only keeps track of the n most important items. If the heap grows in size to more than n items the least important item is dropped.

import unittest

class BinHeap:
    """Creats a binary heap. This is a min heap, meaning that the least largest number is on the root of the tree."""
    def __init__(self, heapSize):
        """Initializes a binary heap"""
        self.heapList = [0]
        self.currentSize = 0
        self.heapSize = heapSize

    def percUp(self, i):
        """Percolates a value up if it is smaller than its parent"""
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        """Inserts an item into the Binary Heap."""
        if self.currentSize < heapSize:
            self.heapList.append(k)
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)
        else:
            self.heapList.append(k)
            self.percUp(self.currentSize)
            self.delMin()

    def percDown(self, i):
        """Percolates an item down into the binary heap"""
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        """Finds the minimum child in the binary heap, the root."""
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        """Deletes the minimum of the binary heap"""
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        """Builds a heap"""
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        if self.currentSize > self.heapSize:
            for i in range(self.currentSize-self.heapSize):
                self.delMin()
        else:
            return
        
class testBinaryHeap(unittest.TestCase):
    """Tests to make sure that the binary heap is working."""

    def testParseTree(self):
        """Acts as a main driver for the program, tests binary heap"""
        heap = BinHeap(5)
        heap.buildHeap([1,2,3,5,6,7,8])
        print(heap.delMin())
        print(heap.delMin())
        print(heap.delMin())
        print(heap.delMin())


if __name__ == '__main__':
    unittest.main()
