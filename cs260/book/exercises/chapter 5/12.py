# 12: Modify the Tower of Hanoi program using turtle graphics to animate the movement of the disks. Hint: You can make multiple turtles and have them shaped like rectangles.

import turtle
import unittest

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
    showTower(fromPole.size(),withPole.size(),toPole.size())
    """Moves tower"""
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    """Moves disk"""
    tp.push(fp.pop())
    print("moving disk from",fp,"to",tp)

def showTower(tower1,tower2,tower3):
    """Represents the current state of the hanoi problem with Turtle graphics"""
    t1c1 = turtle.Turtle()
    t2c1 = turtle.Turtle()
    t3c1 = turtle.Turtle()
    t1c2 = turtle.Turtle()
    t2c2 = turtle.Turtle()
    t3c2 = turtle.Turtle()
    t1c3 = turtle.Turtle()
    t2c3 = turtle.Turtle()
    t3c3 = turtle.Turtle()
    t1c1.penup()
    t2c1.penup()
    t3c1.penup()
    t1c2.penup()
    t2c2.penup()
    t3c2.penup()
    t1c3.penup()
    t2c3.penup()
    t3c3.penup()
    t1c1.goto(0,0)
    t2c1.goto(100,0)
    t3c1.goto(200,0)
    t1c2.goto(0,100)
    t2c2.goto(100,100)
    t3c2.goto(200,100)
    t1c3.goto(0,200)
    t2c3.goto(100,200)
    t3c3.goto(200,200)
    t1c1.pendown()
    t1c2.pendown()
    t1c3.pendown()
    t2c1.pendown()
    t2c2.pendown()
    t2c3.pendown()
    t3c1.pendown()
    t3c2.pendown()
    t3c3.pendown()
    if tower1 == 1:
        t1c1.forward(50)
    elif tower1 == 2:
        t1c1.forward(50)
        t1c2.forward(75)
    elif tower1 == 3:
        t1c1.forward(50)
        t1c2.forward(75)
        t1c3.forward(100)
    if tower2 == 1:
        t2c1.forward(50)
    elif tower2 == 2:
        t2c1.forward(50)
        t2c2.forward(75)
    elif tower2 == 3:
        t2c1.forward(50)
        t2c2.forward(75)
        t2c3.forward(100)
    if tower3 == 1:
        t3c1.forward(50)
    elif tower3 == 2:
        t3c1.forward(50)
        t3c2.forward(75)
    elif tower3 == 3:
        t3c1.forward(50)
        t3c2.forward(75)
        t3c3.forward(100)
    

class test(unittest.TestCase):
    """Tests the code, acts as a main driver."""
    moveTower(3,Stack(),Stack(),Stack())

if __name__ == '__main__':
    unittest.main()