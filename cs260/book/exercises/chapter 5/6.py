# 6. Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks.

class Stack:
    """Implements a stack"""
    def __init__(self):
        """Intializes an empty stack."""
        self.items = []

    def isEmpty(self):
        """Returns true if empty."""
        return self.items == []

    def push(self, item):
        """Pushes an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pops an item from the stack."""
        return self.items.pop()

    def peek(self):
        """Peeks at an item on the stack."""
        return self.items[len(self.items)-1]

    def size(self):
        """Returns size of the stack."""
        return len(self.items)

def moveTower(height,fromPole, toPole, withPole):
    """Moves tower"""
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    """Moves disk"""
    tp.push(fp.pop())
    print("moving disk from",fp,"to",tp)

import unittest

class test(unittest.TestCase):
    """Tests the code, acts as a main driver."""
    fromPole = Stack()
    toPole = Stack()
    withPole = Stack()
    for i in range(5):
        fromPole.push(i)
    moveTower(5,fromPole,toPole,withPole)

if __name__ == '__main__':
    unittest.main()