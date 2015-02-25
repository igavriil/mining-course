import GraphModule as g


def graphToLaplacianMatrix(graph):
    A = g.graphToAdjMatrix(graph)
    D = g.graphToDegreeMatrix(graph)
    L = D - A
    return L
