#9: Modify the Hot Potato simulation to allow for a randomly chosen counting value so that each pass is not predictable from the previous one.

import random

class Queue:
    """Abstract Queue implementation, order is LIFO."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

#this is my "unit test". I can't reliably test this with a traditional unit test because the output is random.
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],random.randint(1,15)))

