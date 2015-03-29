import numpy as np


def map_function(M, v):
    x_dim, y_dim = M.shape
    map_dict = {}
    for i in range(0, x_dim):
        values = []
        for j in range(0, y_dim):
            values.extend(M[i, j]*v[j])
        map_dict[i+1] = values
    return map_dict


def reduce_function(map_dict):
    x = np.zeros((len(map_dict.keys()), 1))
    for k, v in map_dict.iteritems():
        x[k-1] = sum(v)
    return x

M = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
v = np.array([[1], [2], [3], [4]])

map_dict = map_function(M, v)
print map_dict
print reduce_function(map_dict)

print np.dot(M, v)
