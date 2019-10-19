def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

print(gcd(20,10))

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(gcd(20,10),10)

if __name__ == '__main__':
    unittest.main()