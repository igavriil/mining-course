import sympy as sym


M = sym.Matrix([[1, 1], [2, 2], [3, 4]])
sym.pprint(M)
sym.pprint(M.T)
M_tran_dot_M = M.T*M
sym.pprint(M_tran_dot_M)
eigenvectors = M_tran_dot_M.eigenvects()
sym.pprint(eigenvectors)
firsteig = sym.simplify(eigenvectors[0][2:3][0][0])
secondeig = sym.simplify(eigenvectors[1][2:3][0][0])
sym.pprint(firsteig)
sym.pprint(secondeig)
E = sym.Matrix([[firsteig[0], secondeig[0]], [firsteig[1], secondeig[1]]])
