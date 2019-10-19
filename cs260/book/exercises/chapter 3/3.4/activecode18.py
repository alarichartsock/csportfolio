def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(anagramSolution2('abcde','edcba'),True)

if __name__ == '__main__':
    unittest.main()