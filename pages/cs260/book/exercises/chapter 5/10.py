# 10: Generalize the problem above so that the parameters to your solution include the sizes of each jug and the final amount of water to be left in the larger jug.

class Jug():
    """Jug class, represents a jug."""
    def __init__(self,capacity):
        """Initializes a jug"""
        self.capacity = capacity
        self.water = 0

    def getCapacity(self):
        return self.capacity

    def emptyInto(self,intoJug):
        """Empty the jug into another jug"""
        self.water = intoJug.fill(self.water)

    def empty(self):
        """Empty the jug onto the ground"""
        self.water = 0

    def isFull(self):
        """Returns true if the water is full"""
        return self.water == self.capacity

    def fill(self, water):
        """Fills the jug, returns the excess water."""
        if self.water < self.capacity:
            if water <= (self.capacity - self.water): #If water doesn't overflow the second jug
                self.water = self.water + water
                return 0
            else: #If water overflows the second jug
                previouswater = self.water
                self.water = self.capacity
                return water + previouswater - (self.water)
                
        else:
            print("Jug is filled.")
        return
    
    def getWater(self):
        """Returns the amount of water in jug. Do not use this function during the problem, only for unit testing."""
        return self.water

def jugProblem(bigJug,smallJug,amountDesired):
    """Represents the jug problem from the chapter. amountDesired must be smaller than the capacity of bigJug, and larger than the smallJug"""
    if amountDesired > bigJug.getCapacity():
        print("Too much desired.")
        return
    elif amountDesired < bigJug.getCapacity():
        bigJug.fill(bigJug.getCapacity())
        bigJug.emptyInto(smallJug) #1 gal left in big jug
        smallJug.empty()
        bigJug.emptyInto(smallJug) #1 gal in jug 3
        bigJug.fill(4)
        bigJug.emptyInto(smallJug)
        print(bigJug.getWater())

import unittest

class test(unittest.TestCase):
    """Tests the code, acts as a main driver."""
    def testJug(self):
        jug1 = Jug(4)
        jug2 = Jug(3)
        jug1.fill(4)
        jug1.emptyInto(jug2)
        self.assertEqual(jug1.getWater(),1)
        jugProblem(Jug(5),Jug(3),4)

if __name__ == '__main__':
    unittest.main()

main()


