import numpy as np
import itertools as it


# wagner fisher algorithm
def editDistance(firstWord, secondWord):
    m = len(firstWord)+1
    n = len(secondWord)+1
    distMarix = np.zeros((m, n))
    for i in xrange(m):
        distMarix[i, 0] = i
    for j in xrange(n):
        distMarix[0, j] = j
    for i in xrange(1, m):
        for j in xrange(1, n):
            if firstWord[i-1] == secondWord[j-1]:
                distMarix[i, j] = distMarix[i-1, j-1]
            else:
                # allow only inserts and deletes
                distMarix[i, j] = min(distMarix[i-1, j]+1, distMarix[i, j-1]+1)
    return distMarix[m-1, n-1], distMarix


words = ['he', 'she', 'his', 'hers']

for pair in it.combinations(words, 2):
    d, m = editDistance(pair[0], pair[1])
    print 'pair {}-{}:distance {}'.format(pair[0], pair[1], d)
