import matplotlib.pyplot as plt
from decimal import *
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import kMeansModule as km


fig = plt.figure()
plt.axis([20, 70, 0, 150])
ax = fig.add_subplot(111)

green_points = [(25, 125), (44, 105), (29, 97), (35, 63), (55, 63), (42, 57), (23, 40), (64, 37), (33, 22), (55, 20)]
yellow_points = [(28, 145), (65, 140), (50, 130), (38, 115), (55, 118), (50, 90), (63, 88), (43, 83), (50, 60), (50, 30)]

km.plot_points(green_points, yellow_points, ax, 'go', 'yo')

centroid_to_points = km.all_nearest_neighboor(green_points, yellow_points)
neighbourhoods = km.create_neighbourhoods(centroid_to_points)

km.plot_connections(centroid_to_points, 'k--')

centroids = km.neighbourhoods_centroid(neighbourhoods)
km.plot_centroids(centroids, ax, 'rx')

centroid_to_points = km.all_nearest_neighboor(centroids, yellow_points)
km.plot_connections(centroid_to_points, 'y-')


plt.show()
