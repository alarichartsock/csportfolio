myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(myList[2],45)

if __name__ == '__main__':
    unittest.main()