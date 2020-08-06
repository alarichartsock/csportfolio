# Modify the recursive tree program using one or all of the following ideas:

#     Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.

#     Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.

#     Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.

#     Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.

# If you implement all of the above ideas you will have a very realistic looking tree.

import turtle
import random

def tree(branchLen,t,):
    """Draws a tree recursively with the Python Turtle library."""
    if branchLen > 5:
        t.pensize(branchLen/5)
        if(branchLen<30):
            t.color("green")
        else:
            t.color("black")
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-random.randint(10,20),t)
        t.left(40)
        tree(branchLen-random.randint(10,20),t)
        t.right(20)
        t.backward(branchLen)

import unittest

class test(unittest.TestCase):
    """Tests the code, acts as a main driver."""
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("black")
    tree(75,t)
    myWin.exitonclick()

if __name__ == '__main__':
    unittest.main()