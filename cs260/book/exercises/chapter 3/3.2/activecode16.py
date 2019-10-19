def sumOfN3(n):
   return (n*(n+1))/2

print(sumOfN3(10))

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(sumOfN3(10),55)

if __name__ == '__main__':
    unittest.main()