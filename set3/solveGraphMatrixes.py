import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import GraphModule as g
import numpy as np

graph = g.jsonToGraph('graph3-1.json')

A = g.graphToAdjMatrix(graph, beta=1, normalize=True)
D = g.graphToDegreeMatrix(graph)
L = g.graphToLaplacianMatrix(graph)


def sumAndNoneZero(matrix, name='matrix'):
    elemSum = np.sum(matrix)
    nonZero = np.count_nonzero(matrix)
    print '{}: sum = {} - non zero = {}'.format(name, elemSum, nonZero)
print A
sumAndNoneZero(A, 'Adjacent')
print D
sumAndNoneZero(D, 'Degree')
print L
sumAndNoneZero(L, 'Laplace')
