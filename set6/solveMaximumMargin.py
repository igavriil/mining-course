import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import symbols
import numpy as np

p1 = (5, 4)
p2 = (8, 3)
p3 = (7, 2)
p4 = (3, 3)
pos_points = [p1, p2]
neg_points = [p3, p4]

fig = plt.figure()
plt.axis([0, 9, 0, 5])
ax = fig.add_subplot(111)

pos_points_x, pos_points_y = map(list, zip(*pos_points))
neg_points_x, neg_points_y = map(list, zip(*neg_points))

plt.plot(pos_points_x, pos_points_y, 'ro')
plt.plot(neg_points_x, neg_points_y, 'bo')

for i, j in pos_points + neg_points:
    ax.annotate('({:.1f},{:.1f})'.format(i, j), xy=(i, j+0.1))

w1, w2, b = symbols("w1 w2 b")


def find_max_margin_pos_neg(pos_points, neg_point):
    x1, y1 = pos_points[0]
    x2, y2 = pos_points[1]
    x3, y3 = neg_point
    f1 = x1 * w1 + y1 * w2 + b - 1
    f2 = x2 * w1 + y2 * w2 + b - 1
    f3 = x3 * w1 + y3 * w2 + b + 1
    sol = solve((f1, f2, f3), w1, w2, b)
    return sol[b], sol


def find_max_margin_neg_pos(neg_points, pos_point):
    x1, y1 = neg_points[0]
    x2, y2 = neg_points[1]
    x3, y3 = pos_point
    f1 = x1 * w1 + y1 * w2 + b + 1
    f2 = x2 * w1 + y2 * w2 + b + 1
    f3 = x3 * w1 + y3 * w2 + b - 1
    sol = solve((f1, f2, f3), w1, w2, b)
    return sol[b], sol

solutions = {}
b1, sol1 = find_max_margin_neg_pos(neg_points, pos_points[0])
solutions[abs(b1)] = sol1
b2, sol2 = find_max_margin_neg_pos(neg_points, pos_points[1])
solutions[abs(b2)] = sol2
b3, sol3 = find_max_margin_pos_neg(pos_points, neg_points[0])
solutions[abs(b3)] = sol3
b4, sol4 = find_max_margin_pos_neg(pos_points, neg_points[1])
solutions[abs(b4)] = sol4
print solutions
max_margin = solutions[max(solutions)]
print max_margin


def line(x):
    return (-max_margin[w1]*x - max_margin[b])/max_margin[w2]

def graph(line, x_range):
    x = np.array(x_range)
    y = line(x)
    plt.plot(x, y)


graph(line, range(0, 10))
plt.show()
