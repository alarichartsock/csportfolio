# 7: Clean up the printexp function so that it does not include an ‘extra’ set of parentheses around each number.
import unittest

class BinaryTree:
    """Implementation for a Binary Tree"""
    def __init__(self, rootObj):
        """Initializes a binary tree"""
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """Inserts a left child"""
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        """Inserts a right  child"""
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """Gets right child"""
        return self.rightChild

    def getLeftChild(self):
        """Gets left child"""
        return self.leftChild

    def setRootVal(self, obj):
        """Sets root value"""
        self.key = obj

    def getRootVal(self):
        """Gets root value"""
        return self.key

def printexp(tree):
    """Prints the tree"""
    sVal = ""
    if tree:
        sVal = printexp(tree.getLeftChild()) + " "
        sVal = sVal + str(tree.getRootVal()) + " "
        sVal = sVal + printexp(tree.getRightChild())
    return sVal

class testBinaryTree(unittest.TestCase):
    """Tests to make sure that the binary tree is working."""

    def testParseTree(self):
        """Acts as a main driver for the program, tests binary heap"""
        r = BinaryTree('a')
        r.insertLeft('b')
        r.insertRight('c')
        r.getRightChild().setRootVal('hello')
        print(printexp(r))

if __name__ == '__main__':
    unittest.main()