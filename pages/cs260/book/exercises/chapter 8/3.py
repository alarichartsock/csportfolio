#3: Write the transpose method for the Graph class.

import unittest

class Vertex:
    """Vertex Implementation. A Vertex holds data within a graph"""
    def __init__(self,key):
        """Initializes a graph"""
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        """Adds a neightbor to a vertex"""
        self.connectedTo[nbr] = weight

    def __str__(self):
        """OVerrides the tostring method."""
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """Returns the other vertexes that the vertex is connected to"""
        return self.connectedTo.keys()

    def getId(self):
        """Returns vertex ID"""
        return self.id

    def getWeight(self,nbr):
        """Returns vertex weight"""
        return self.connectedTo[nbr]

class Graph:
    """Graph implementation"""
    def __init__(self):
        """Initializes a Graph"""
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        """Adds a vertex to the Graph"""
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        """Gets a Vertex from the graph"""
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        """Overrides contains method on Graph"""
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        """Adds an edge to the graph"""
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        """Returns vertices from graph"""
        return self.vertList.keys()

    def __iter__(self):
        """Overrides iterable method for graph"""
        return iter(self.vertList.values())

    def show(self):
        """Prints out graph vetices."""
        for k,v in self.vertList.items():
            print(v)
    
    def transpose(self):
        """Flips the edges between the vertices on the graph"""
        d = []
        for k,v in self.vertList.items():
            for b in v.getConnections():
                weight = v.getWeight(b)
                d.append((b.getId(),v.getId(),weight)) #f,t,weight
        # for i in range(len(d)):
        #     print(d[i][0] + " to " + d[i][1])
        #     print(d[i][2])
        self.nuke()
        for i in range(len(d)):
            self.addEdge(d[i][0],d[i][1],d[i][2])

    def nuke(self):
        """Deletes vertices"""
        self.vertList.clear()
        self.numVertices = 0
        

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
        print("new ones after transpose:")
        g.transpose()
        g.show()

if __name__ == '__main__':
    unittest.main()

