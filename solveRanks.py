import GraphModule as g
from decimal import *

graph = g.jsonToGraph('graph.json')

# print graph.getVertices()
# for v in graph.getVertices().values():
#     for n in v.getNeighboors():

g.setInitialRanks(graph)
A = g.graphToAdjMatrix(graph, beta=1, normalize=True)

x = g.initialVector(graph, uniform=False)
print A
print x
x = g.nextArray(x, A, iterations=10)
