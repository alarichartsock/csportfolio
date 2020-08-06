#8: Using the turtle graphics module, write a recursive program to display a Koch snowflake.

from turtle import *
import unittest

def KochSnowflake(levels,length):
    """Draws a koch snowflake"""
    if levels <= 0:
        forward(length)
        return
    length = length / 3.0
    KochSnowflake(length,levels-1)
    left(60)
    KochSnowflake(length,levels-1)
    right(120)
    KochSnowflake(length,levels-1)
    left(60)
    KochSnowflake(length,levels-1)

import unittest

class test(unittest.TestCase):
    """Tests the code, acts as a main driver."""
    left(180)
    penup()
    forward(300)
    left(90)
    forward(300)
    left(90)
    pendown()
    KochSnowflake(8,200)

if __name__ == '__main__':
    unittest.main()

main()

