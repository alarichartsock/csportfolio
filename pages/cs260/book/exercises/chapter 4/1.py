# 1. Modify the infix-to-postfix algorithm so that it can handle errors.

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
    
print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):
        self.assertEqual(infixToPostfix("A * B + C * D"),"A B * C D * +")
        
if __name__ == '__main__':
    unittest.main()
