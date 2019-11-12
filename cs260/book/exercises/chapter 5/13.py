#13: Write a program that prints out Pascal’s triangle. Your program should accept a parameter that tells how many rows of the triangle to print.
import unittest

def pascalsTriangle(n,current):
    """Prints out n steps of pascals triangle. Current is the steps that it starts printing out at, so this can actually print a slice of pascal's triangle."""
    if n == current:
        print(pascalsRow(n))
    else:
        print(pascalsRow(current))
        pascalsTriangle(n,current+1)

def pascalsRow(n):
    """Prints out an nth row of pascal's triangle."""
    s = ""
    for i in range(0,n+1):
        s = s + str(pascalsRule(n,i)) + ", "
        f = "[ " +  s + "]"
    return f

def pascalsRule(n,k):
    """Returns a number according to pascals rule given a specific row and column. The row is n and the column is k."""
    return (factorial(n) / (factorial(k) * factorial(n-k)))

def factorial(n):
    """Recursive function to evaluate a factorial number, n"""
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)

class test(unittest.TestCase):
    """Tests the code, acts as a main driver."""
    def test(self):
        print(pascalsTriangle(15,0))
        self.assertTrue(pascalsRow(3),[ 1.0, 3.0, 3.0, 1.0, ])

if __name__ == '__main__':
    unittest.main()