def sumOfN(n):
   theSum = 0
   for i in range(1,n+1):
       theSum = theSum + i

   return theSum

print(sumOfN(10))

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(sumOfN(10),55)

if __name__ == '__main__':
    unittest.main()