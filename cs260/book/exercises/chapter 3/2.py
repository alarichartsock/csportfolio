#2
#Running this section shows you that the big O of get method of a dictonary is 1. As we increase the complexity of our input, even to an insane number, we see that the time to get is the same.
import time
from collections import defaultdict # Only way to automatically populate a dictionary is to import defaultdict.

dictionary = defaultdict(list)

def set_up_dictionary(O):
    for i in range(O):
        dictionary['example'].append(("example",1))

set_up_dictionary(1000000)

def time_decorator(fn):
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

@time_decorator
def TestDictionaryGet(O):
    """Testing the big O of the List Index method"""
    dictionary.get(O)
    return O

print(TestDictionaryGet(100))
print(TestDictionaryGet(1000))
print(TestDictionaryGet(10000))
print(TestDictionaryGet(100000))
print(TestDictionaryGet(1000000))

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):
        self.assertTrue(dictionary['example'],1)
        
if __name__ == '__main__':
    unittest.main()
