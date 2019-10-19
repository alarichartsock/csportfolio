aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(),
      "and has length", len(aName))

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(len(aName.upper()),len(aName))

if __name__ == '__main__':
    unittest.main()
