import numpy as np


def create_link_matrix(graph):
    dim = len(graph)
    L = np.zeros((dim, dim))
    for from_node, to_node in graph.iteritems():
        L[from_node, to_node] = 1
    return L


def initialize_hubbiness(graph):
    dim = len(graph)
    h = np.ones((dim, 1))
    return h


def normalize(vector):
    largest = np.max(vector)
    return np.true_divide(vector, largest)


def estimate_hubinness(L, a):
    h = normalize(np.dot(L, a))
    return h


def estimate_authority(L, h):
    a = normalize(np.dot(L.T, h))
    return a


def converg(v_new, v_old, target):
    if np.sum(np.square(np.subtract(v_new, v_old))) < target:
        return True
    else:
        return False

graph = {0: [1, 2], 1: [0], 2: [3], 3: [2]}


L = create_link_matrix(graph)
h_old = initialize_hubbiness(graph)

while True:
    a_new = estimate_authority(L, h_old)
    h_new = estimate_hubinness(L, a_new)
    if 'a_old' in locals():
        if converg(a_new, a_old, 1e-10) and converg(h_new, h_old, 1e-10):
            break
    a_old = a_new
    h_old = h_new

print "authority"
print a_new
print "hubbiness"
print h_new
