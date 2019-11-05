# 2: Modify the postfix evaluation algorithm so that it can handle errors.

class Stack:
    """Abstract Stack implementation in Python."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []   
    def push(self, item):
        self.items.append(item)   
    def pop(self):
        return self.items.pop()   
    def peek(self):
        return self.items[len(self.items)-1]  
    def size(self):
        return len(self.items)

def postfixEval(postfixExpr):
    """Evaluates a postfix expression using PEMDAS"""
    operandStack = Stack()
    tokenList = postfixExpr.split()

    try:
        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(token,operand1,operand2)
                operandStack.push(result)
        return operandStack.pop()
    except IndexError:
        print("Invalid input. Please try again")

def doMath(op, op1, op2):
    """Evaluates based on operand"""
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):
        self.assertEqual(postfixEval('7 8 + 3 2 + /'),3.0)
        
if __name__ == '__main__':
    unittest.main()

