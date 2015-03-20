import numpy as np

M = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
v = np.array([[1], [2], [3], [4]])
x_dim, y_dim = M.shape
map_dict = {}
for i in range(0, x_dim):
	values = []
	for j in range(0, y_dim):
		values.extend(M[i,j]*v[j])
	map_dict[i+1] = values
print map_dict	