import matplotlib.pyplot as plt
from decimal import *
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import kMeansModule as km


fig = plt.figure()
plt.axis([0, 24, 0, 24])
ax = fig.add_subplot(111)

centroids = [(5, 10), (20, 5)]
c1UL = (7,12) #(6, 7)(6, 15) (3, 15)  
c1LR = (12, 8) #(11, 14)(13, 7) (13, 7) 
c1LL = (c1UL[0], c1LR[1])
c1UR = (c1LR[0], c1UL[1])

c2UL = (16, 16) #(16, 16) (11,5)(11,5) 
c2LR = (18, 5) #(18, 5) (17,2) (17, 2) 
c2LL = (c2UL[0], c2LR[1])
c2UR = (c2LR[0], c2UL[1])

points = [c1UL, c1LR, c1LL, c1UR, c2UL, c2LR, c2LL, c2UR]

km.plot_points(centroids, points, ax, 'go', 'yo')

centroid_to_points = km.all_nearest_neighboor(centroids, points)
neighbourhoods = km.create_neighbourhoods(centroid_to_points)

km.plot_connections(centroid_to_points, 'k--')

plt.show()
