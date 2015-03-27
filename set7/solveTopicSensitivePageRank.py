import numpy as np
from fractions import Fraction

graph = {0:[1, 2], 1 : [0], 2: [3], 3:[2]}

dim = len(graph.keys())

M = np.zeros((dim,dim))
for from_node, to_node in graph.iteritems():
	M[to_node, from_node] = Fraction(1, len(graph[from_node]))

print M
beta = Fraction(7, 10)

M = beta*M
teleport_set = {0: 2, 1: 1}

teleport_arr = np.zeros((dim, 1))
v = np.zeros((dim, 1))
v_new = np.zeros((dim, 1))


for page, weight in teleport_set.iteritems():
	teleport_arr[page, 0] = Fraction(weight, len(teleport_set))
	v[page, 0] = Fraction(1, len(teleport_set))

print teleport_arr
teleport_arr[:,0] = teleport_arr[:,0]/sum(teleport_arr)
teleport_arr = (1 - beta)* teleport_arr

print teleport_arr
while True:
	v_new = np.dot(M, v) + teleport_arr
	if np.sum(abs(v_new - v)) < 1e-10:
		break
	v = v_new

print v_new
