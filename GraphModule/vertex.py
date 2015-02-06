class Vertex:

    def __init__(self, key, colour="white", rank=1):
        self.id = key
        self.colour = colour
        self.rank = rank
        self.neighboors = {}

    def getRank(self):
        return self.rank

    def getId(self):
        return self.id

    def getColour(self):
        return self.colour

    def setColour(self, colour):
        self.colour = colour

    def setRank(self, rank):
        self.rank = rank

    def addNeighboor(self, vertex, weight=0):
        self.neighboors[vertex.getId()] = {'vertex': vertex, 'weight': weight}

    def getNeighboors(self):
        return self.neighboors.values()

    def __str__(self):
        return str(self.id)
