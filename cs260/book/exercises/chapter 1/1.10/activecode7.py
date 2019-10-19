wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(letterlist[0],"c")

if __name__ == '__main__':
    unittest.main()
