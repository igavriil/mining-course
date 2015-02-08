import numpy as np


def split_and_create_buckets(signatureMatrix, numberOfBands):
    signatureMatrix = np.vsplit(signatureMatrix, numberOfBands)
    canditates = [dict() for x in range(numberOfBands)]
    for i, subarray in enumerate(signatureMatrix):
        print subarray
        for column in xrange(subarray.shape[1]):
            bucket = np.array_str(subarray[:, column])
            canditates[i].setdefault(bucket, []).append(column+1)
    return canditates

signatureMatrix = np.array([[1, 2, 1, 1, 2, 5, 4], [2, 3, 4, 2, 3, 2, 2], [3, 1, 2, 3, 1, 3, 2], [4, 1, 3, 1, 2, 4, 4], [5, 2, 5, 1, 1, 5, 1], [6, 1, 6, 4, 1, 1, 4]])

canditates = split_and_create_buckets(signatureMatrix, 3)
for bucket, canditate in enumerate(canditates):
    print bucket, canditate
