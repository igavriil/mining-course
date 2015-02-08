import numpy as np


def norm(point1, point2, norm_type):
    differences = point1 - point2
    absolute_differences = np.abs(differences)
    power_distance = np.power(absolute_differences, norm_type)
    sum_distance = np.sum(power_distance)
    distance = np.power(sum_distance, 1.0/norm_type)
    return distance


def nearestNeighboor(points, searchPoints, norm_type):
    for testPoint in searchPoints:
        min_distance = np.inf
        for point in points:
            distance = norm(point, testPoint, norm_type)
            if distance < min_distance:
                min_distance, nearest_neigh = distance, point
            # print 'L{} distance from :{} to :{} is {}'.format(norm_type, point, testPoint, distance)
        print 'nearest neighboor of {} is {} with distance {} and L{} norm'.format(testPoint, nearest_neigh, min_distance, norm_type)

point1 = np.array([0, 0])
point2 = np.array([100, 40])

trainingPoints = (point1, point2)

testPoint1 = np.array([55, 5])
testPoint2 = np.array([52, 13])
testPoint3 = np.array([61, 8])
testPoint4 = np.array([56, 15])

testPoints = (testPoint1, testPoint2, testPoint3, testPoint4)

for i in range(1, 1+2):
    nearestNeighboor(trainingPoints, testPoints, i)
