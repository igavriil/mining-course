import numpy as np


array = np.array([[0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 0]])

values = np.arange(1, array.shape[0]+1, 1)
minhash = np.array([4, 6, 1, 3, 5, 2])
signature = np.empty(array.shape[1])
signature[:] = np.NAN


array = array*values[:, None]
print array

for i, rows in enumerate(minhash):
    index = np.where(minhash == i+1)[0][0]
    if np.count_nonzero(np.isnan(signature)) == 0:
        break
    for i, item in enumerate(array[index]):
        if item != 0:
            if np.isnan(signature[i]):
                signature[i] = item
            elif signature[i] > item:
                signature[i] = item

print signature
