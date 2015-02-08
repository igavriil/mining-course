import numpy as np


def norm(point1, point2, norm_type):
    differences = point1 - point2
    absolute_differences = np.abs(differences)
    power_distance = np.power(absolute_differences, norm_type)
    sum_distance = np.sum(power_distance)
    distance = np.power(sum_distance, 1.0/norm_type)
    return distance


point1 = np.array([0, 0])
point2 = np.array([100, 40])

testPoint1 = np.array([55, 5])
testPoint2 = np.array([52, 13])
testPoint3 = np.array([61, 8])
testPoint4 = np.array([56, 15])

testPoints = (testPoint1, testPoint2, testPoint3, testPoint4)
for point in testPoints:
    print '--- point {} ---'.format(point)
    L1point1 = norm(point1, point, 1)
    L1point2 = norm(point2, point, 1)
    L2point1 = norm(point1, point, 2)
    L2point2 = norm(point2, point, 2)
    print 'L1 distance from 1- {} and 2- {}'.format(L1point1, L1point2)
    print 'L1 norm to {}'.format(point1 if L1point1 < L1point2 else point2)
    print 'L2 distance from 1- {} and 2- {}'.format(L2point1, L2point2)
    print 'L2 norm to {}'.format(point1 if L2point1 < L2point2 else point2)
   
