class Edge:

    def __init__(self, startVertex, endVertex, weight=0):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight

    def getStartVertex(self):
        return self.startVertex

    def getEndVertex(self):
        return self.endVertex

    def getWeight(self):
        return self.weight

    def __str__(self):
        return str(self.startVertex) + '-' + str(self.endVertex)
