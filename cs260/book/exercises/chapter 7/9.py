# 9: Write a function that takes a parse tree for a mathematical expression and calculates the derivative of the expression with respect to some variable.

#todo: get help for this.

import re
import string
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


class Queue:
    """A queue data type, implements first in first out"""

    def __init__(self):
        """Initializes a queue"""
        self.items = []

    def isEmpty(self):
        """Returns true if is empty"""
        return self.items == []

    def enqueue(self, item):
        """Puts an item in the queue"""
        self.items.insert(0, item)

    def dequeue(self):
        """Takes an item out of the queue"""
        return self.items.pop()

    def size(self):
        """Returns the size of the queue"""
        return len(self.items)
    
    def show(self):
        """Prints out the queue"""
        l = ""
        for i in range(self.size()):
            l = self.items[i] + l
        return l


class BinaryTree:
    def __init__(self, rootObj):
        """Initializes a Binary Tree"""
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """Inserts left of the binary tree."""
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        """Inserts right in the binary search tree"""
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """Gets the right child of the tree"""
        return self.rightChild

    def getLeftChild(self):
        """Gets the left child of the tree"""
        return self.leftChild

    def setRootVal(self, obj):
        """Sets the root value of the tree"""
        self.key = obj

    def getRootVal(self):
        """Returns the root value of the Tree"""
        return self.key


def split(word):
    """Splits each input into a list of its characters, disreguards whitespace."""
    return [char for char in word if char is not " "]


def buildParseTree(fpexp):
    """Implementation for a parse tree, acts as a calculator. Accepts expressions with whitespace and non whitespace."""
    fplist = re.split("([+-/*])",fpexp)
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                i = str(i)
                if i in (string.ascii_lowercase or string.ascii_uppercase) and ["1","2","3","4","5","6","7","8","9","10"]:
                    r = ""
                    for l in len(i):
                        if i[l] in ["1","2","3","4","5","6","7","8","9","10"]:
                            r =  r + i[l]
                        else:
                            pass
                    currentTree.setRootVal(r)
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

def inorder(tree):
  """Prints an inorder traversal of the tree"""
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

class testInsertionSort(unittest.TestCase):
    """Tests to make sure that the evaluation is working."""
    def testParseTree(self):
        """Acts as a main driver for the program, tests buildParseTree"""
        pt = buildParseTree("10x + 5y * 3r")
    
        print(inorder(pt))
        
        
if __name__ == '__main__':
    unittest.main()

