# 3 - Devising an experiment that compares the performance of delete operators on Lists and Dictionaries

import time
from collections import defaultdict # Only way to automatically populate a dictionary is to import defaultdict.

#Setting up the List version

List = []
def set_Up_List(O):
    for i in range(O+1):
        List.append(1)
        
set_up_list(10000000);

def time_decorator(fn):
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

#Setting up the dictionary version

dictionary = defaultdict(list)

def set_up_dictionary(O):
    for i in range(O+1):
        dictionary[i].append(i)

set_up_dictionary(1000000)

#Testing them both

@time_decorator
def TestListDelete(O):
    """Testing the big O of the List Index method"""
    del List[O]
    return O

print(TestListDelete(100))
print(TestListDelete(1000))
print(TestListDelete(10000))
print(TestListDelete(100000))
print(TestListDelete(1000000))


@time_decorator
def TestDictionaryDelete(O):
    """Testing the big O of the List Index method"""
    del dictionary[O]
    return O

print(TestDictionaryDelete(100))
print(TestDictionaryDelete(1000))
print(TestDictionaryDelete(10000))
print(TestDictionaryDelete(100000))
print(TestDictionaryDelete(1000000))

#As we can see, the O of del for Dictionary is O(1) and the O of the list del is more complex. This is the data on my machine.

"""(100, 0.002992391586303711)
(1000, 0.003989458084106445)
(10000, 0.002991914749145508)
(100000, 0.0029921531677246094)
(1000000, 0.003989458084106445)
(100, 0.0)
(1000, 0.0)
(10000, 0.0)
(100000, 0.0)
(1000000, 0.0)"""

#The experiment might be different on your machine. Mine is getting some weird data for the first point, but the overall trend looks to be O(n).
#Here's a more detailed experiment that creates more data points. 

def testListDeleteMoreAccurately(O):
    for i in range(O):
        print(TestListDelete(i*100))

print(testListDeleteMoreAccurately(100))

#When I plot this on a graph, I get 4 clusters ranging from .003 to .006 time to execute. 
#I actually think that my machine is interfering with the experiment by subdividing tasks to different cores to try to get the program to run as fast as possible.

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):
        self.assertTrue(List[0],1)
        
if __name__ == '__main__':
    unittest.main()
