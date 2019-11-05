# 4. Turn your direct infix evaluator from the previous problem into a calculator.

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


def infixToPostfix(infixexpr):
    """Converts infix to postfix expressions."""
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    try: 
        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)
    except KeyError:
        print("Invalid input.")

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

def infixEval(infixExpr):
    """Evaluates an infix expression"""
    return postfixEval(infixToPostfix(infixExpr))

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):
        self.assertEqual(infixEval("7 + 7 - 6"),8)
        
if __name__ == '__main__':
    unittest.main()