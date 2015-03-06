import numpy as np
from itertools import combinations


def norm(point1, point2, norm_type):
    differences = point1 - point2
    absolute_differences = np.abs(differences)
    power_distance = np.power(absolute_differences, norm_type)
    sum_distance = np.sum(power_distance)
    distance = np.power(sum_distance, 1.0/norm_type)
    return distance


def max_distance(points):
    max_dist = 0
    all_comb = map(list, combinations(points, 2))
    for combination in all_comb:
        dist = norm(combination[0], combination[1], 2)
        if dist > max_dist:
            max_dist = dist
            max_pair = combination
    return max_dist, max_pair


def furthest(starts, points):
    search_points = [p for p in points if all(any(p != q) for q in starts)]
    point_dist = {}
    for point in search_points:
        min_dist = np.inf
        for start in starts:
            dist = norm(start, point, 2)
            # print dist, point
            if dist < min_dist:
                min_dist = dist
        point_dist[min_dist] = point
    max_val = max(point_dist.keys())
    return {k: v for k, v in point_dist.iteritems() if k == max_val}

x = np.array([0, 0])
y = np.array([10, 10])
a = np.array([1, 6])
b = np.array([3, 7])
c = np.array([4, 3])
d = np.array([7, 7])
e = np.array([8, 2])
f = np.array([9, 5])
points = [x, y, a, b, c, d, e, f]

centroids = []
max_dist, max_pair = max_distance(points)
centroids.extend(max_pair)
i = 1
while len(centroids) < len(points):
    point_dist = furthest(centroids, points)
    print point_dist
    centroids.append(point_dist.values()[0])
    print "{} added {}".format(i, point_dist)
    i += 1
    
