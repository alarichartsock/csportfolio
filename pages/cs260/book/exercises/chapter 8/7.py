#7: Generalize the problem above so that the parameters to your solution include the sizes of each jug and the final amount of water to be left in the larger jug.

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

class Jug():
    """Jug class, represents a jug."""
    def __init__(self,capacity):
        """Initializes a jug"""
        self.capacity = capacity
        self.water = 0

    def getCapacity(self):
        return self.capacity

    def emptyInto(self,intoJug):
        """Empty the jug into another jug"""
        self.water = intoJug.fill(self.water)

    def empty(self):
        """Empty the jug onto the ground"""
        self.water = 0

    def isFull(self):
        """Returns true if the water is full"""
        return self.water == self.capacity

    def fill(self, water):
        """Fills the jug, returns the excess water."""
        if self.water < self.capacity:
            if water <= (self.capacity - self.water): #If water doesn't overflow the second jug
                self.water = self.water + water
                return 0
            else: #If water overflows the second jug
                previouswater = self.water
                self.water = self.capacity
                return water + previouswater - (self.water)
                
        else:
            print("Jug is filled.")
        return
    
    def getWater(self):
        """Returns the amount of water in jug. Do not use this function during the problem, only for unit testing."""
        return self.water

def transitions(jug1, jug2, jug1_size, jug2_size):
    """Return all possible transitions in water from a single input."""
    transitions = []

    # Fill jug 1.
    if jug1 < jug1_size:
        transitions.append((jug1_size,jug2))

    # Fill jug 2.
    if jug2 < jug2_size:
        transitions.append((jug1,jug2_size))

    # Pour jug 1 to jug 2.
    measure = min(jug1, jug2_size - jug2)
    if measure > 0:
        if jug1 > jug2:
            transitions.append((jug1-jug2,jug2_size))
        else:
            transitions.append((0,jug1))

    # Pour jug 2 to jug 1.
    measure = min((jug1_size - jug1, jug2))
    if measure > 0:
        if jug2 > jug1:
            if jug1 + jug2 <= jug1_size:
                transitions.append((jug1+jug2,0))
            else: 
                transitions.append((jug1_size,jug1+jug2-jug1_size))
        else:
            transitions.append((jug1-jug2,jug2_size))
        transitions.append((jug1+measure,jug2-measure))

    # Empty jug 1.
    if jug1 > 0:
        transitions.append((0,jug2))

    # Empty jug 2.
    if jug2 > 0:
        transitions.append((jug1,0))

    return transitions

def build_gallon_graph(jug1, jug2, jug1_size, jug2_size):
    """Builds a graph representing the problem."""
    q = Queue()
    g = Graph()
    finished = False
    currNode = Vertex((4,3))
    q.enqueue(currNode)
    while finished == False:
        currNode = q.dequeue()
        g.addVertex(currNode)
        if currNode.getId()[0] == 4:
            finished = True
            print("Finished the problem")
        paths = transitions(currNode.getId()[0], currNode.getId()[1], jug1_size, jug2_size)
        for answer in paths:
            g.addEdge(currNode,(answer[0],answer[1]),1)
            print(str(answer[0]) + ", " + str(answer[1]))
        for i in g.getVertex(currNode).getConnections():
            q.enqueue(i)
            # q.enqueue((new_jug1,new_jug2))
        
class testDFS(unittest.TestCase):
    """Tests to make sure that the water program is working."""

    def testDFS(self):
        """Acts as a main driver for the water program"""
        build_gallon_graph(0,0,4,3)

if __name__ == '__main__':
    unittest.main()


