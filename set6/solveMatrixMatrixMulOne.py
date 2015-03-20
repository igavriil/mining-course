import numpy as np
from collections import defaultdict

M = np.array([[1, 2], [3, 4], [5, 6]])
N = np.array([[1, 2, 3 ,4], [5, 6, 7, 8]])
print M
print N
print np.dot(M, N)

def map_function(M, N):
	M_rows, M_cols = M.shape
	N_rows, N_cols = N.shape

	MN_dict = defaultdict(list)

	for i in range(0, M_rows):
		# columns
		for j in range(0, M_cols):
			for k in range(0, N_cols):
				MN_dict[(i+1, k+1)].append(('M', j+1, M[i, j]))
				# M_dict[(i+1, k+1)] = ('M', j+1, M[i, j])
	# rows
	for j in range(0, N_rows):
		# columns
		for k in range(0, N_cols):
			for i in range(0, M_rows):
				MN_dict[(i+1, k+1)].append(('N', j+1, N[j, k]))
	return MN_dict

MN_dict = map_function(M, N)
for key, value in MN_dict.iteritems():
	print len(value)