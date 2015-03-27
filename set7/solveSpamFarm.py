import sympy as sym

beta, y, m, n, x, k= sym.symbols('beta y m n x k')

second_tear_page_rank = beta*y/k + (1-beta)/n
supporting_page_rank = beta*second_tear_page_rank/(m/k) +(1-beta)/n
supporting_page_rank = beta**2*y/m + beta*(1-beta)*k/m*n + (1-beta)/n
outside_contribution = x


y = x + m*beta*supporting_page_rank 
y = x + beta**3*y + beta**2*(1-beta)*k/n + beta*(1-beta)*m/n
y = x /(1 - beta**3) + (beta**2*(1-beta)/(1 - beta**3))*k/n + (beta*(1-beta)/(1 - beta**3))*m/n

	
b = 0.85

print "a is {}".format((1 - b**3))
print "b is {}".format((b*(1-b)/(1 - b**3)))
print "c is {}".format((b**2*(1-b)/(1 - b**3)))