import numpy as np
c = np.array([2.0/7.0, 3.0/7.0, 6.0/7.0])
# c = np.array([1, 2, 3])

print c
print np.linalg.norm(c)

test1 = np.array([-.548, .401, .273])
test2 = np.array([.312, .156, -.937])
test3 = np.array([.429, .857, .286])
test4 = np.array([-.297, .890, -.346])
# test1 = np.array([-1, -2, -3])
# test2 = np.array([4, 2, -1])
# test3 = np.array([-4, -1, 2])
# test4 = np.array([-3, -2, 5])

test_columns = [test1, test2, test3, test4]
for test_column in test_columns:
    print test_column
    print "norm:{}".format(np.linalg.norm(test_column))
    print "dot:{}".format(np.dot(c, test_column))
