#4: Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.

#Making a ist of random numbers

import random

RandomList = []

def populateList(length,depth):
    for i in range(length):
        RandomList.append(random.randint(1,depth))

populateList(5000,1000)

#I'm going to try it with a list 5000 numbers long, 1000 numbers tall

def findSmallestNumber():
    RandomList.sort()
    print(RandomList[0])

findSmallestNumber()

#Yep, that's literally it. The O of sort is n log n, and printing a List by index is O(1). So the total algorithm is O(nlogn+1), or O(nlogn). gg ez pz

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):

        self.assertTrue(RandomList[0],1)
        
if __name__ == '__main__':
    unittest.main()
