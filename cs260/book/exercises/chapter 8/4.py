# 4: Using breadth first search write an algorithm that can determine the shortest path from each vertex to every other vertex. This is called the all pairs shortest path problem.

import unittest

class Vertex:
    """Implements a Vertex class, used in the Graph ADT."""
    def __init__(self,key):
        """Initializes a Vertex."""
        self.id = key
        self.connectedTo = {}
        self.color = "White"
        self.finish = 0
        self.discovery = 0

    def replaceNeighbors(self,newneighbors):
        """Replaces the connectedTo dictionary."""
        self.connectedTo = newneighbors

    def addNeighbor(self,nbr,weight=0):
        """Adds a neighbor to the Vertex."""
        self.connectedTo[nbr] = weight

    def __str__(self):
        """Overrides the toString method."""
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """Returns connections that the vertex holds."""
        return self.connectedTo.keys()

    def getConnectionsDetailed(self):
        """Exposes the connectedTo dictionary"""
        return self.connectedTo

    def removeConnection(nbr):
        """Removes a connection from the Vertex"""
        del self.connectedTo[nbr]

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
        """Sets finish for Node according to ADT"""
        self.finish = finish

class Graph:
    """Graph implementation using the Vertex class."""
    def __init__(self):
        """Initializes a graph class."""
        self.vertList = {}
        self.numVertices = 0
    
    def show(self):
        """Prints off all vertices and their neightbors on the graph."""
        for k,v in self.vertList.items():
            print(k)
            print(v)

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
        return self.vertList()

    def __iter__(self):
        """Overrides and iterates over Graph class."""
        return iter(self.vertList.values())

class testDFS(unittest.TestCase):
    """Tests to make sure that the dfs is working."""

    def testDFS(self):
        """Acts as a main driver for the program, tests dfs"""
        g = Graph()
        g.addVertex("a")
        g.addVertex("b")
        g.addVertex("c")
        g.addVertex("d")
        g.addVertex("e")
        g.addVertex("f")
        g.addEdge("a","b",1)
        g.addEdge("a","d",2)
        g.addEdge("b","c",3)
        g.addEdge("d","e",4)
        g.addEdge("e","b",5)
        g.addEdge("e","f",6)
        g.addEdge("f","c",7)
        print("old ones:")
        g.show()
        g.transpose()
        print("new ones:")
        g.show()

if __name__ == '__main__':
    unittest.main()

