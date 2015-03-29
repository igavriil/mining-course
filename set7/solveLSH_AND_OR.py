import sympy as sym


def and_construction(h, fucntion_count):
    d1 = h["d1"]
    d2 = h["d2"]
    p1 = h["p1"]**fucntion_count
    p2 = h["p2"]**fucntion_count
    return {"d1": d1, "d2": d2, "p1": p1, "p2": p2}


def or_construction(h, fucntion_count):
    d1 = h["d1"]
    d2 = h["d2"]
    p1 = (1-(1 - h["p1"]**fucntion_count))
    p2 = (1-(1 - h["p2"]**fucntion_count))
    return {"d1": d1, "d2": d2, "p1": p1, "p2": p2}


d1, d2 = sym.symbols('d1 d2')

h = {"d1": d1, "d2": d2, "p1": 0.6, "p2": 0.4}
print "w is {:.3f} and x is {:.3f}".format(and_construction(h, 3)["p1"],and_construction(h, 3)["p2"])
print "y is {:.3f} and z is {:.3f}".format(or_construction(h, 2)["p1"],or_construction(h, 2)["p2"])