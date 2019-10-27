# 1. Write a recursive function to compute the factorial of a number

def factorial(n):
    """Recursively computes the factorial of a number."""
    if n==1:
        return n
    else:
        return n * factorial(n-1)

import unittest

class test(unittest.TestCase):
    def testFactorial(self):
        """Tests that the factorial function is working correctly."""
        self.assertTrue(factorial(5),120)
        self.assertTrue(factorial(6),720)
        self.assertTrue(factorial(7),5040)
        
if __name__ == '__main__':
    unittest.main()