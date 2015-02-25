import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import GraphModule as g
import numpy as np

graph = g.jsonToGraph('graph3-2.json')

L = g.graphToLaplacianMatrix(graph)

eigenValues, eigenVectors = np.linalg.eig(L)
idx = eigenValues.argsort()
# sort eigenVector in asceding eigenValue
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[idx, :]
print eigenValues
print eigenVectors

secondEigen = eigenVectors[1, :]
print '-- second Laplacian eigenVector --'
print secondEigen
print '-- mean value of the eigenVector --'
mean = np.average(secondEigen)
print mean
print '-- clustering nodes based on mean value -- '
for i, value in enumerate(secondEigen):
    if value > mean:
        print 'node {} in cluster A'.format(i+1)
    else:
        print 'node {} in cluster B'.format(i+1)
