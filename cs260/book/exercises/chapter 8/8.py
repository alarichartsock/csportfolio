#8: Write a program that solves the following problem: Three missionaries and three cannibals come to a river and find a boat that holds two people. Everyone must get across the river to continue on the journey. However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of crossings that will get everyone safely to the other side of the river. 

import unittest

class Queue:
    """Traditional Queue implementation from runestone.academy."""
    def __init__(self):
        """Initializes Queue"""
        self.items = []

    def isEmpty(self):
        """Checks if the Queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Adds an item to the queue"""
        self.items.append(item)

    def dequeue(self):
        """Removes an item from the queue"""
        return self.items.pop()

    def size(self):
        """Returns total size of Queue"""
        return len(self.items)
    
    def show(self):
        """Prints the queue"""
        print(self.items)
        return

class Vertex:
    """Implements a Vertex class, used in the Graph ADT."""
    def __init__(self,key):
        """Initializes a Vertex."""
        self.id = key
        self.connectedTo = {}
        self.color = "White"
        self.finish = 0
        self.discovery = 0

    def addNeighbor(self,nbr,weight=0):
        """Adds a neighbor to the Vertex."""
        self.connectedTo[nbr] = weight

    def __str__(self):
        """Overrides the toString method."""
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """Returns connections that the vertex holds."""
        return self.connectedTo.keys()

    def getId(self):
        """Returns Vertex ID."""
        return self.id

    def getWeight(self,nbr):
        """Returns the vertex weight."""
        return self.connectedTo[nbr]

    def setColor(self,color):
        """Sets the color according to DFS ADT"""
        self.color = color

    def getColor(self):
        """Returns color of a node according to ADT implementation"""
        return self.color
    
    def setPred(self,pred):
        """Sets a predacessor for the Node according to ADT"""
        self.pred = pred
    
    def setDiscovery(self,discovery):
        """Sets discovery for Node according to ADT"""
        self.discovery = discovery

    def setFinish(self,finish):
        """Sets finish for Node accoridn got ADT"""
        self.finish = finish

class Graph:
    """Graph implementation using the Vertex class."""
    def __init__(self):
        """Initializes a graph class."""
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        """Adds a Vertex to the graph"""
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        """Gets a Vertex from the Graph"""
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        """Returns true if there is vertex in the Graph class."""
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        """Adds an edge to the Graph class."""
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        """Gets Vertices from the Graph."""
        return self.vertList.keys()

    def __iter__(self):
        """Overrides and iterates over Graph class."""
        return iter(self.vertList.values())

def genLegalMoves(x , y , z):
    """Generates legal moves"""
    newMoves = []
    moveOffsets = set((x, y, z) for x in range(-2,2) for y in range(-2,2) for z in range(0,2))
    # print(moveOffsets)
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        newZ = z + i[2]
        if legalMove(newX, newY, newZ) and (newX+newY) - (x+y) <= 2:
            newMoves.append((newX, newY, newZ))
    return newMoves

def legalMove(x,y,z):
    """Determines if a move is legal or not."""
    if x < y:
        return False
    if x == 3 and y == 3 and z == 2:
        return False
    if x == 0 and y == 0 and z == 1:
        return False
    if x >= 2 and y < 2:
        return False
    if x > 3 or y > 3 or z > 2:
        return False
    if x < 0 or y < 0 or z < 1:
        return False
    if x == 1 and y == 0:
        return False
    else:
        return True

def genId(xyz):
    """Generates an ID for the Vertex class."""
    s = str(xyz[0]) + str(xyz[1]) + str(xyz[2])
    return s

def solveProblem():
    """Main driver for most of the code. Implements a depth first search to branch out possible steps"""
    q = Queue()
    g = Graph()
    finished = False
    currNode = Vertex((3,3,1))
    q.enqueue(currNode)
    while finished == False:
        currNode = q.dequeue()
        print(currNode.getId())
        g.addVertex(currNode)
        if currNode.getId() == "002":
            finished = True
        answers = genLegalMoves(int(currNode.getId()[0]),int(currNode.getId()[1]),int(currNode.getId()[2]))
        for i in answers:
            g.addEdge(currNode,genId(i),1)
            print("making branch " + genId(i))
        for i in g.getVertex(currNode).getConnections():
            q.enqueue(i)

class testDFS(unittest.TestCase):
    """Tests to make sure that the dfs is working."""

    def testDFS(self):
        """Acts as a main driver for the program, tests dfs"""
        solveProblem()

if __name__ == '__main__':
    unittest.main()

#Output:
#331
#221
#111
#002