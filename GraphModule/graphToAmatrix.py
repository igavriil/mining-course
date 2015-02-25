from fractions import Fraction
import numpy as np


def setInitialRanks(graph):
    for v in graph.getVertices().values():
        v.setRank(Fraction(1, len(v.getNeighboors())))
    return graph


def graphToAdjMatrix(graph, beta=1, normalize=False):
    size = len(graph.getVertices())
    if normalize:
        mult = Fraction(1, size)
    else:
        mult = 1
    A = np.ones((size, size))*(1-beta)*mult
    vertices = graph.getVertices()
    for v in vertices.values():
        column = vertices.keys().index(v.getId())
        for n in v.getNeighboors():
            row = vertices.keys().index(n['vertex'].getId())
            A[row, column] += beta*v.getRank()
    return A


def initialVector(graph, uniform=True):
    size = len(graph.getVertices())
    if uniform:
        mult = Fraction(1, size)
    else:
        mult = 1
    x = np.ones(size).reshape(size, -1) * mult
    return x


def nextArray(vector, matrix, iterations=200, epsilon=1e-5):
    for i in range(iterations):
        newVector = np.dot(matrix, vector)
        diff, vector = ((vector-newVector < epsilon).all(), newVector)
        if i == iterations or diff:
            break
    return vector
