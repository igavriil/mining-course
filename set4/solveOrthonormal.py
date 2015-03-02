import sympy as sym
from fractions import Fraction

for i in range(0,3):
    print i
    if i==0:
        x, y = sym.symbols('x y')
        z = sym.sqrt(1-x**2-y**2)
        mul = 2
    elif i==1:
        x, z = sym.symbols('x z')
        y = sym.sqrt(1-x**2-z**2)
        mul = Fraction(-3, 2)
    else:
        y, z = sym.symbols('y z')
        x = sym.sqrt(1-y**2-z**2)
        mul = Fraction(-1, 3)

    a = sym.Matrix([[Fraction(2, 7), Fraction(6, 7), x], [Fraction(3, 7), Fraction(2, 7), y], [Fraction(6, 7), Fraction(-3, 7), z]])


    con1 = sym.simplify(a.col(0).dot(a.col(2)))
    con2 = sym.simplify(a.col(1).dot(a.col(2)))
    sym.pprint(con1)
    sym.pprint(con2)
    sym.pprint(sym.simplify(con1+mul*con2))
