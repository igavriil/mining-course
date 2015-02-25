import numpy as np


def graphToDegreeMatrix(graph):
    size = len(graph.getVertices())
    D = np.zeros((size, size))
    vertices = graph.getVertices()
    for v in vertices.values():
        index = vertices.keys().index(v.getId())
        value = len(v.getNeighboors())
        D[index, index] = value
    return D
