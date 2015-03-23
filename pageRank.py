import numpy as np
import scipy.sparse as sparse
import fileinput
from collections import defaultdict
import copy

class page_Rank():
	def __init__(self):
		self.from_nodes = set()
		self.to_nodes = set()
		self.nodes = set()
		self.count = None

	def read_file(self, filename):
		self.out_link_count = defaultdict(lambda: 0)
		self.point_to = defaultdict(list)
		for line in fileinput.input([filename]):
			if not line.startswith('#'):
				fromNode, toNode = map(int, str.split(line))
				self.from_nodes.add(fromNode)
				self.to_nodes.add(toNode)
				self.out_link_count[fromNode] += 1
				self.point_to[toNode].append(fromNode)	
		self.nodes = self.from_nodes | self.to_nodes
				
	def preproccess(self):
		self.v = {}
		self.v_new = {}
		self.point_to_link_count = defaultdict(list)
		self.count = len(self.nodes)
		for toNode in self.nodes:
			for fromNode in self.point_to[toNode]:
				self.point_to_link_count[toNode].append(self.out_link_count[fromNode])
			self.v[toNode] = 1.0/ self.count

	def check(self):
		e = 0
		print '-----'	
		for toNode in self.nodes:
			temp_sum = abs(self.v[toNode] - self.last_v[toNode])
			e += temp_sum
		return e > 1e-10


	def find_next(self, beta):
		self.last_v = copy.copy(self.v)
		for toNode in self.nodes:	
			if toNode in self.point_to:
				d_i = self.point_to_link_count[toNode]
				r_i = []
				
				for i in self.point_to[toNode]:
					r_i.append(self.v[i])
				self.v_new[toNode] = np.sum(beta*np.divide(r_i, d_i))
			else:
				self.v_new[toNode] = 0.0
		S = np.sum(self.v_new.values())
		for toNode in self.nodes:
			self.v[toNode] = self.v_new[toNode] + (1.0-S)/self.count

	def print_me(self):
		# print self.out_link_count
		# print self.point_to
		# print self.point_to_link_count
		# print self.from_nodes
		# print self.to_nodes
		# print self.count
		# print self.v, np.sum(self.v.values())
		# print self.v_new, np.sum(self.v_new.values())
		print self.v[99]



p = page_Rank()	
p.read_file("web-Google.txt")

p.preproccess()
i = 0
while True:
	p.find_next(0.8)
	i += 1
	print i
	if not p.check():
		break

print p.check()
p.print_me()


# from_node = []
# to_node = []
# i = 0
# out_links = defaultdict(lambda: 0)
# for line in fileinput.input(['web-Google.txt']):
# 	if not line.startswith('#'):
# 		f, t = map(int, str.split(line))
# 		out_links[f] += 1
# 		from_node.append(f)
# 		to_node.append(t)
		
		

# row_A = np.array(to_node)
# col_A = np.array(from_node)
# (N, ) = row_A.shape 


# data_A = np.array([1]*N)
# shape_A = (row_A.max(axis = 0)+1, col_A.max(axis = 0)+1)
# print row_A.shape
# print col_A.shape
# print data_A.shape
# print shape_A

# A = sparse.coo_matrix((data_A, (row_A, col_A)), shape = shape_A)


# # = col_A.shape

# row_r = np.unique(np.concatenate((row_A, col_A)))
# (N, ) = row_r.shape 
# col_r = np.array([0]*N)
# data_r = np.array([1.0/N]*N)
# shape_r = (row_A.max(axis = 0)+1, 1)
# print row_r.shape
# print col_r.shape
# print data_r.shape
# print shape_r

# r = sparse.csr_matrix((data_r, (row_r, col_r)), shape = shape_r)
# r_new = sparse.lil_matrix(r)


# # get all the nodes pointing to j by simply picking all
# # nonzero elements in the j-th row of Adjacency Matrix
# def have_link_to(j):
# 	(_, i) = A.getrow(j).nonzero()
# 	return i


# # get the sparse column with the corresponding r_j
# # convert it to an array transpose it so it becomes a row
# # and squeeze it to lose it's dimensionality and become 1Dra
# def vector_values(nodes):
# 	return np.squeeze(r[nodes].toarray().T)


# # for all the nodes pointing to j create and array with
# # each ones out degree
# def out_degree(nodes):
# 	return np.array([out_links[i] for i in nodes])


# # calculate the fraction r_i/d_i for all the nodes i
# # pointing to j and sum them up
# def new_vector_value(j, pointing_to_j, d_i, beta):
# 	# pointing_to_j = have_link_to(j)
# 	if pointing_to_j.size:
# 		r_i = vector_values(pointing_to_j)
# 		# d_i = out_degree(pointing_to_j)
# 		return beta*np.sum(np.divide(r_i, d_i))
# 	else:
# 		return 0.0

# # fix some standart values
# to_nodes, _ = r_new.nonzero()
# pointing_to = {}
# out_degree_pointing_to = {}
# for j in to_nodes:
# 	pointing_to[j] = have_link_to(j)
# 	out_degree_pointing_to[j] = out_degree(pointing_to[j])
# print pointing_to
# print out_degree_pointing_to

# for j in to_nodes:
# 	v_new = new_vector_value(j,pointing_to[j], out_degree_pointing_to[j], 0.8)
# 	r_new[j, 0] = v_new
# 	print j, v_new	

# S = r_new.sum()
# print S
# to_nodes, _ = r.nonzero()
# for j in to_nodes:
# 	v = r_new[j, 0] + (1-S)/N
# 	r[j, 0] = v
# 	print j, v	




