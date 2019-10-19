def foo(tom):
    fred = 0
    for bill in range(1,tom+1):
       barney = bill
       fred = fred + barney

    return fred

print(foo(10))

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(foo(10),55)

if __name__ == '__main__':
    unittest.main()