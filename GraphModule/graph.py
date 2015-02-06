class Graph:
    def __init__(self):
        self.vertexDict = {}
        self.edgeList = []

    def addVertex(self, vertex):
        if vertex.getId() not in self.vertexDict.keys():
            self.vertexDict[vertex.getId()] = vertex
            return vertex

    def addEdge(self, edge, undirected=True):
        startVertex = self.addVertex(edge.getStartVertex())
        if not startVertex:
            startVertex = self.vertexDict[edge.getStartVertex().getId()]

        endVertex = self.addVertex(edge.getEndVertex())
        if not endVertex:
            endVertex = self.vertexDict[edge.getEndVertex().getId()]

        startVertex.addNeighboor(endVertex, edge.getWeight())
        if undirected:
            endVertex.addNeighboor(startVertex, edge.getWeight())
        self.edgeList.append(edge)

    def getVertex(self, key):
        return self.vertexDict[key]

    def getVertices(self):
        return self.vertexDict

    def getEdges(self):
        return self.edgeList
