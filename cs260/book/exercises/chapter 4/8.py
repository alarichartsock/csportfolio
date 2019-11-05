#8. Consider a real life situation. Formulate a question and then design a simulation that can help to answer it. Possible situations include:
#Cars lined up at a car wash
#Customers at a grocery store check-out
#Airplanes taking off and landing on a runway
#A bank teller
#Be sure to state any assumptions that you make and provide any probabilistic data that must be considered as part of the scenario.


#I'm gonna do cars lined up at a car wash.

class ModifiedQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)
        return

import unittest

class testCars(unittest.TestCase):
    def testQueue(self):
        """Tests a real world scenario, in this case a car wash using the queue data structure.."""
        q = ModifiedQueue()
        q.enqueue("car1")
        q.enqueue("car2")
        q.enqueue("car3")
        q.show()
        q.dequeue()
        q.show()
        q.enqueue("car4")
        q.enqueue("car5")
        q.enqueue("car6") # it's a busy day
        q.show()
        q.dequeue()
        q.dequeue()
        q.dequeue() #the guy got off of his lunch break and started washing cars
        q.show() # 2 more
        self.assertTrue(q.size(),2)
        q.dequeue
        q.dequeue
        self.assertTrue(q.isEmpty,True)

        
if __name__ == '__main__':
    unittest.main()