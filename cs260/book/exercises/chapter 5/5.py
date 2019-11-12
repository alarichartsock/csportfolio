# 5. Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive function compare to that of an iterative version?

def fibrecusively(n):
    """This will print out the nth term of the fibbonaci sequence recursively."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibrecusively(n-1)+fibrecusively(n-2)

def fibtraditional(n):
    """This will print out the nth term of the fibbonaci sequence without recursion."""
    n1 = 0;
    n2 = 1;
    count = 0;
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(n-1):
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return nth
        
#Already, there is way more assignent with the traditional function. I think that the recursive function is going to do much better

import unittest
import time

class test(unittest.TestCase):
    def testQueue(self):
        """Tests to make sure that the fibonacci functions are working correctly."""
        self.assertTrue(fibtraditional(5),5)
        self.assertTrue(fibrecusively(5),5)
        self.assertTrue(fibrecusively(6),8)
        self.assertTrue(fibrecusively(6),8)

#if __name__ == '__main__':
#    unittest.main()

def time_decorator(fn):
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

@time_decorator
def TestRecursive(O):
    """Test the Big O of the fibonacci recursive function"""
    fibrecusively(O)
    return O

@time_decorator
def TestTraditional(O):
    """Test the Big O of the fibonacci traditional function"""
    fibtraditional(O)
    return O

def testRecursiveAccurately(O):
    """Tests recursion accurately."""
    for i in range(O):
        print(TestRecursive(i))

def testTraditionalAccurately(O):
    """Tests traditional accurately."""
    for i in range(O):
        print(TestTraditional(i))

print(testRecursiveAccurately(30))
print(testTraditionalAccurately(70))

#Wow, my prediction was completely wrong. The recursive function was the inefficient one. The traditional function absolutely blew it out of the water. I have no idea why.