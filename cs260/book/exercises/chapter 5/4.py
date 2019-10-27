# 4. Find or invent an algorithm for drawing a fractal mountain. Hint: One approach to this uses triangles again.

import turtle
import random

def mountain (x, y, complexity, turtleName):
    """Draws the mountain"""
    if complexity == 0:
        turtleName.setposition(x, y)
    else: 
        x1 = (turtleName.xcor() + x)/2
        y1 = (turtleName.ycor() + y)/2
        y1 = y1 + (random.uniform(0, complexity) - 0.5) * (turtleName.xcor() - x)
        complexity = complexity - 1
        mountain(x1, y1, complexity, turtleName)
        mountain(x, y, complexity, turtleName)


def main ():
    """Collects input for the mountain drawing function"""
    #Gets input for first coordinate pair, splits, and assigns to variables
    coordinate = str(input("Enter the coordinate pair, separated by a comma: "))
    x, y = coordinate.split(',')
    x = int(x)
    y = int(y)

    complexity = int(input("Enter the complexity: "))
    while complexity < 0:
        complexity = int(input("Input must be positive. Enter the complexity: "))

    Bob = turtle.Turtle()
    mountain(x, y, complexity, Bob)

main ()

import unittest

class test(unittest.TestCase):
    self.assertTrue(1,1)
    
# if __name__ == '__main__':
#     unittest.main()