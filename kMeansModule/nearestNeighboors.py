import matplotlib.pyplot as plt
import operator, itertools
from decimal import *
import numpy as np


getcontext().prec = 6

def norm(point1, point2, norm_type):
    differences = point1 - point2
    absolute_differences = np.abs(differences)
    power_distance = np.power(absolute_differences, norm_type)
    sum_distance = np.sum(power_distance)
    distance = np.power(sum_distance, 1.0/norm_type)
    return distance


def all_nearest_neighboor(centroids, points):
    all_neigh = []
    for point in points:
        x, y = point
        p = np.array([x, y])
        min_distance = np.inf
        for centroid in centroids:
            cx, cy = centroid
            cp = np.array([cx, cy])
            distance = norm(p, cp, 2)
            if distance < min_distance:
                min_distance, nearest_neigh = distance, cp
        all_neigh.append((tuple(p), tuple(nearest_neigh)))
    return all_neigh


def create_neighbourhoods(centroid_close_to_points):
    neighbours = centroid_close_to_points
    centroids = set(map(lambda x: x[1], neighbours))
    neighbourhoods = [[y[0] for y in neighbours if y[1] == x] for x in centroids]
    for neigh, cent in zip(neighbourhoods, centroids):
        neigh.append(cent)
    return neighbourhoods


def neighbourhoods_centroid(neighbourhoods):
    centroids = []
    for neighbourhood in neighbourhoods:
        count = len(neighbourhood)
        x, y = map(list, zip(*neighbourhood))
        sum_x, sum_y = sum(x), sum(y)
        centroids.append((float(sum_x)/count, float(sum_y)/count))
    return centroids


def plot_connections(centroid_close_to_points, colour):
    for point, centroid in centroid_close_to_points:
        x_coords, y_coords = map(list, zip(point, centroid))
        plt.plot(x_coords, y_coords, colour, lw=1)


def plot_points(centroids, points, axis, centroid_col, point_col):
    centroids_x, centroids_y = map(list, zip(*centroids))
    points_x, points_y = map(list, zip(*points))

    plt.plot(centroids_x, centroids_y, centroid_col)
    plt.plot(points_x, points_y, point_col)

    for i, j in centroids + points:
        axis.annotate('({:.1f},{:.1f})'.format(i, j), xy=(i, j+0.5))


def plot_centroids(centroids, axis, centroid_col):
    centroids_x, centroids_y = map(list, zip(*centroids))   
    plt.plot(centroids_x, centroids_y, centroid_col)
    for i, j in centroids:
        axis.annotate('({:.1f},{:.1f})'.format(i, j), xy=(i, j+0.5))