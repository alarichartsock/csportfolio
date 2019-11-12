#1: Running this section shows you that the big O of index method of a list is 1. As we increase the complexity of our input, even to an insane number, we see that the time to index is the same.
import time

List = []
def set_up(O):
    """Sets up the experiment"""
    for i in range(O):
        List.append(1)
set_up(10000000);


def time_decorator(fn):
    """Sets up basic timekeeping"""
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

@time_decorator
def TestListIndex(O):
    """Testing the big O of the List Index method"""
    List.index(1,0,O)
    return O

print(TestListIndex(100))
print(TestListIndex(1000))
print(TestListIndex(10000))
print(TestListIndex(100000))
print(TestListIndex(10000000))

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):
        """Basic test for the List class"""
        self.assertTrue(List[0],1)
        
if __name__ == '__main__':
    unittest.main()
