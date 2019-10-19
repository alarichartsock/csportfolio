print(5==10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(10>5,true)
if __name__ == '__main__':
    unittest.main()