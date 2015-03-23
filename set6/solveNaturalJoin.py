from collections import defaultdict

R = [(0, 1), (1, 2), (2, 3)]
S = [(0, 1), (1, 2), (2, 3)]

def map_function(R, S):
	map_dict = defaultdict(list)
	for (a, b) in R:
		map_dict[b].append(('R', a))
	for (b, c) in S:
		map_dict[b].append(('S', c))
	return map_dict

map_dict = map_function(R, S)
print map_dict

def reduce_function(map_dict):
	x = []
	for key, val in map_dict.iteritems():
		if len(val) == 2:
			x.append((key, val))
	return x

print reduce_function(map_dict)