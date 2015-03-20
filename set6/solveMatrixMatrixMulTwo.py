
import numpy as np
from collections import defaultdict

M = np.array([[1, 2], [3, 4], [5, 6]])
N = np.array([[1, 2, 3 ,4], [5, 6, 7, 8]])
print M
print N
print np.dot(M, N)

def first_map_function(M, N):
	M_rows, M_cols = M.shape
	N_rows, N_cols = N.shape

	MN_dict = defaultdict(list)

	for i in range(0, M_rows):
		for j in range(0, M_cols):
			MN_dict[j+1].append(('M', i+1, M[i, j]))

	for j in range(0, N_rows):
		for k in range(0, N_cols):
			MN_dict[j+1].append(('N', k+1, N[j, k]))

	return MN_dict


def first_reduce_function(first_map):
	reduce_dict = defaultdict(list)
	for key, val in first_map.iteritems():
		M_list, N_list = split_values(val)
		print M_list, N_list
		for M_elem in M_list:
			for N_elem in N_list:
				reduce_dict[(M_elem[1], N_elem[1])].append(M_elem[2] * N_elem[2])

	return reduce_dict


def split_values(values_array):
	M_list = []
	N_list = []
	for value in values_array:
		if value[0] == "M":
			M_list.append(value)
		elif value[0] == "N":
			N_list.append(value)
	return M_list, N_list


first_map = first_map_function(M, N)
# print first_map
print len(first_reduce_function(first_map).keys())