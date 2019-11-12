# 7: Using the turtle graphics module, write a recursive program to display a Hilbert curve.

import turtle
import unittest

def Hilbert_curve(A,rule,t,n):
    """Draws a hilbert curve"""
    if n>=1:
        if rule:
            t.left(90)
            Hilbert_curve(A,not rule,t, n-1)
            t.forward(A)
            t.right(90)
            Hilbert_curve(A, rule,t, n-1)
            t.forward(A)
            Hilbert_curve(A,rule,t, n-1)
            t.right(90)
            t.forward(A)
            Hilbert_curve(A,not rule,t, n-1)
            t.left(90)
        else:
            t.right(90)
            Hilbert_curve(A,rule,t, n-1)
            t.forward(A)
            t.left(90)
            Hilbert_curve(A,not rule,t, n-1)
            t.forward(A)
            Hilbert_curve(A,not rule,t, n-1)
            t.left(90)
            t.forward(A)
            Hilbert_curve(A, rule,t, n-1)
            t.right(90)

import unittest

class test(unittest.TestCase):
    """Tests the code, acts as a main driver."""
    A=10
    t=turtle.Turtle()
    my_win=turtle.Screen()
    n=2
    rule=True
    Hilbert_curve(A,rule,t,n)
    my_win.exitonclick()

if __name__ == '__main__':
    unittest.main()


main()