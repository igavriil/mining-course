R = [(0, 1), (1, 2), (2, 3)]
S = [(0, 1), (1, 2), (2, 3)]

def map_function(R, S):
	R_dict = {}
	S_dict = {}
	for (a, b) in R:
		R_dict[b] = ('R', a)
	for (b, c) in S:
		S_dict[b] = ('S', c)
	return R_dict, S_dict

R_dict, S_dict = map_function(R, S)
print R_dict, S_dict
def reduce_function(R_dict, S_dict):
	x = []
	for key, val in R_dict.iteritems():
		if key in S_dict:
			x.append((val[1], key, S_dict[key][1]))
	return x

print reduce_function(R_dict, S_dict)