import GraphModule as g
from decimal import *

graph = g.jsonToGraph('graph.json')

# print graph.getVertices()
# for v in graph.getVertices().values():
#     for n in v.getNeighboors():

g.setInitialRanks(graph)
A = g.graphToAdjMatrix(graph, beta=1, normalize=True)

vector = g.initialVector(graph, uniform=False)
print "Transition Matrix"
print A
print "initial Vector"
print vector
vector = g.nextArray(vector, A, iterations=10)
print "Solution"
print vector
