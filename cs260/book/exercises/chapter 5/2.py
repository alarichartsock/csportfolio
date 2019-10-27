#2: Write a recursive function to reverse a list

inputList = [1,2,3,4,5]


def reverse(oldList):
    """Reverses a list recursively"""
    newList = []
    if len(oldList) < 1:
        return []
    else:
        return [oldList.pop()] + reverse(oldList)

reversedList = reverse(inputList)

print(reverse(inputList))

import unittest

class test(unittest.TestCase):
    """Tests that the list was reversed correctly."""
    def testFactorial(self):
        self.assertTrue(reversedList,[5,4,3,2,1])

if __name__ == '__main__':
    unittest.main()