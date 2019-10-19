# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        if aletter in letterlist:
            print("already contains")
        else:       
            letterlist.append(aletter)
print(letterlist)

import unittest

class myTest(unittest.TestCase):
    def testMath(self):
        self.assertTrue(letterlist,['c','a','t','d','o','g','r','b','i'])

if __name__ == '__main__':
    unittest.main()
