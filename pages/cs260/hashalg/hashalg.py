import random
import string

# Me and Sam Jadzak worked on this together, that's why our code might look similar.

def hashfunction(value):
    """Hashes a function with minimal collision and most amount of completion"""
    hashvalue = []
    y = 0
    for i in range(len(value)):
        if value[i].isdigit():
            x = int(value[i])
            x = ((x * x) // 7)
            hashvalue.append(x)
            
        else:
            x = ord(value[i])
            x = ((x * x) // 8)
            if x > 1000:
                x = ord(value[i])
                x = (x * (x - 1) // 8)
            else:
                hashvalue.append(x)
    for i in range(len(hashvalue)):
        y = y + hashvalue[i]
    print(hashvalue)
    return (y // 6)

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """Generates random inputs for the hash function"""
    return ''.join(random.choice(chars) for x in range(size))

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):
        """Tests Hash function"""
        hashlist = dict.fromkeys(range(1000))
        collisionTally = 0
        for i in range(1000):
            x = [random.randint(0, 1000)]
            y = hashfunction(random_generator())
            if (hashlist[y] == None):
                hashlist[y] = x
            else:
                collisionTally = collisionTally + 1
        print("Number of collision = ",collisionTally)

if __name__ == '__main__':
    unittest.main()