import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import GraphModule as g
import numpy as np

graph = g.jsonToGraph('graph3-2.json')

L = g.graphToLaplacianMatrix(graph)
eigvals, eigenVectors =  np.linalg.eigh(L)

eigenValues, eigenVectors = np.linalg.eig(L)
print np.linalg.eigvals(L)
idx = eigenValues.argsort()
# sort eigenVector in asceding eigenValue
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:, idx]
print eigenValues
print eigenVectors

secondEigen = eigenVectors[:, 1]
secondEigen = np.where(abs(secondEigen) < 1e-10, 0, secondEigen)
print '-- second Laplacian eigenVector --'
print secondEigen
print '-- mean value of the eigenVector --'
mean = np.average(secondEigen)
print mean
print '-- clustering nodes based on mean value -- '
for i, value in enumerate(secondEigen):
    if value > mean:
        print 'node {} in cluster A'.format(i+1)
    elif value < mean:
        print 'node {} in cluster B'.format(i+1)
    else:
        print 'node {} is tie'.format(i+1)
