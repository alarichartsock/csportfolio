# 4: Modify the code for a binary search tree to make it threaded. Write a non-recursive inorder traversal method for the threaded binary search tree. A threaded binary tree maintains a reference from each node to its successor.

import unittest


class TreeNode:
    """Implementation for a TreeNode, a class that holds a key, a value, and possibly points to two other TreeNodes."""

    def __init__(self, key, val, left=None, right=None, parent=None):
        """Initializes a treeNode with the values provided"""
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.successor = None

    def updateSuccessor(self):
        """Updates the TreeNode's successor field"""
        self.successor = self.findSuccessor()
        return self.successor

    def returnSuccessor(self):
        """Returns successor"""
        return self.successor

    def hasLeftChild(self):
        """Returns true if a treeNode has a left child"""
        return self.leftChild

    def hasRightChild(self):
        """Returns true if a treeNode has a right child"""
        return self.rightChild

    def isLeftChild(self):
        """Returns true if a treenode is a left child"""
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """Returns true if TreeNode is a right child"""
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """Returns true if the treeNode is a root"""
        return not self.parent

    def isLeaf(self):
        """Returns true if the treenode is a leaf"""
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """Returns true if the treeNode has any children"""
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """Returns true if it has both children"""
        return self.rightChild and self.leftChild

    def spliceOut(self):
        """Splices an item out of the Binary search tree"""
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        """Finds the next item in order from itself, typically used for in order traversals and removing an item with two children."""
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        """Finds the smallest value in the binary search tree"""
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def replaceNodeData(self, key, value, lc, rc):
        """Replaces node data with new data"""
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __str__(self):
        return self.payload


class BinarySearchTree:
    """Implements a binary search tree, a high efficiency data structure."""

    def updateSuccessors(self):
        """Notifies every node in the tree that a change has ocurred and makes them modify their successors."""
        if self.size > 0:
            current = self.root.findMin()
            for i in range(self.size):
                current = current.updateSuccessor()
            else:
                return

    def inOrder(self):
        """Returns an in order traversal"""
        res = []
        if self.size > 0:
            current = self.root.findMin()
            for i in range(self.size):
                res.append(str(current))
                current = current.returnSuccessor()
        else:
            return
        return res

    def __init__(self):
        """Initializes a Binary Search Tree"""
        self.root = None
        self.size = 0

    def length(self):
        """Returns number of nodes in Tree"""
        return self.size

    def __len__(self):
        """Overrides the __len__ method so that this can be used in len(bst)"""
        return self.size

    def put(self, key, val):
        """Puts an item, val into the BinarySearchTree. The item will be ordered based on the key, which should correspond to the items value."""
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1
        self.updateSuccessors()

    def _put(self, key, val, currentNode):
        """Recursive method for putting an item into the BinarySearchTree, called from the put method."""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        """Overrides the __setitem__ method so we can now assign items by using []"""
        self.put(k, v)

    def get(self, key):
        """Gets an item from the tree"""
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        """Recursive method for retrieving an item form the binary search tree"""
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        """Overrides the get method so that we can access the tree using traditional square brackets."""
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """Removes an item from the binary search tree"""
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
        self.updateSuccessors()

    def __delitem__(self, key):
        """Overrides the del operator so we can use it."""
        self.delete(key)

    def remove(self, currentNode):
        """Recursively removes an item from the binary search tree."""
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


mytree = BinarySearchTree()
mytree[3] = "red"
mytree[4] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"

print(mytree.inOrder())


class testInsertionSort(unittest.TestCase):
    """Tests to make sure that the evaluation is working."""

    def testParseTree(self):
        """Acts as a main driver for the program, tests buildParseTree"""
        mytree = BinarySearchTree()
        mytree[3] = "red"
        mytree[4] = "blue"
        mytree[6] = "yellow"
        mytree[2] = "at"
        self.assertEqual(mytree.inOrder(), ['at', 'red', 'blue', 'yellow'])


if __name__ == '__main__':
    unittest.main()
