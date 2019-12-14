# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
import unittest


# this heap takes key value pairs, we will assume that the keys are integers
class BinHeap:
    def __init__(self, increasing):
        self.heapList = [0]
        self.current_size = 0
        self.increasing = increasing

    def sort(self):
        print("Sorting")
        return

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)

        while i > 0:
            print(self.heapList, i)
            self.perc_down(i)
            i = i - 1

        print(self.heapList, i)

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)

            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]

            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_up(self, i):
        while i // 2 > 0:

            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]

            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def del_min(self):
        ret_val = self.heapList[1]
        self.heapList[1] = self.heapList[self.current_size]
        self.current_size = self.current_size - 1
        self.heapList.pop()
        self.perc_down(1)
        return ret_val

    def is_empty(self):
        return self.current_size == 0


class FooThing:
    def __init__(self, x, y):
        self.key = x
        self.val = y

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __hash__(self):
        return self.key


class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.theHeap = BinHeap()
        self.theHeap.insert(FooThing(5, 'a'))
        self.theHeap.insert(FooThing(9, 'd'))
        self.theHeap.insert(FooThing(1, 'x'))
        self.theHeap.insert(FooThing(2, 'y'))
        self.theHeap.insert(FooThing(3, 'z'))

    def testInsert(self):
        assert self.theHeap.current_size == 5

    def testDelmin(self):
        assert self.theHeap.del_min().val == 'x'
        assert self.theHeap.del_min().val == 'y'
        assert self.theHeap.del_min().val == 'z'
        assert self.theHeap.del_min().val == 'a'

    def testMixed(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(5)
        assert myHeap.del_min() == 1
        myHeap.insert(2)
        myHeap.insert(7)
        assert myHeap.del_min() == 2
        assert myHeap.del_min() == 5

    def testDupes(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(8)
        myHeap.insert(1)
        assert myHeap.current_size == 4
        assert myHeap.del_min() == 1
        assert myHeap.del_min() == 1
        assert myHeap.del_min() == 8

    def testBuildHeap(self):
        myHeap = BinHeap()
        myHeap.build_heap([9, 5, 6, 2, 3])
        f = myHeap.del_min()
        # print("f = ", f)
        assert f == 2
        assert myHeap.del_min() == 3
        assert myHeap.del_min() == 5
        assert myHeap.del_min() == 6
        assert myHeap.del_min() == 9


if __name__ == '__main__':
    d = {}
    d[FooThing(1, 'z')] = 10
    unittest.main()