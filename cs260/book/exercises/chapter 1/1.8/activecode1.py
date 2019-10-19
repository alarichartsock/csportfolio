print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(3/6)
print(3//6)
print(3%6)
print(2**100)

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(2+3*4,20)
if __name__ == '__main__':
    unittest.main()