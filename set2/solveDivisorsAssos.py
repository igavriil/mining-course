from math import sqrt


def factors(n):
    # create a set so that duplcates are eliminated
    # join two list with reduce
    # add divisors as n modulo i equals 0
    # limit on square root as at worst case the two factor are the same
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))


setA = set([4, 10, 12])
# setB = set([1, 3, 6])
setC = set([8, 12])
setD = set([8, 10])
searchSets = [setA, setC, setD]

for number in range(1, 100):
    number_factors = factors(number)
    subsets = 0
    for search in searchSets:
        if search.issubset(number_factors):
            subsets += 1
            print search
    if subsets != 0:
        print number, sorted(number_factors)
        print '-------------'


