import numpy as np
import matplotlib.pyplot as plt

# v = (5*x) + (7*y)
# base vector: v / (magnitude), labelled i and j
# reversing vector: -v
# multiplying vector with scalar

def magnitude(origin, point):
    x1, y1 = origin
    x2, y2 = point
    x_length = x2 - x1
    y_length = y2 - y1
    mag = ((x_length)**2 + (y_length)**2)**(1/2)
    return mag

v = [2,4]

A = np.array([0, 0, v[0], v[1]])

plt.figure()
plt.ylabel('y-axis')
plt.xlabel('x-axis')
ax = plt.gca()
ax.annotate(f'v({v[0]}, {v[1]})', (v[0], v[1]), fontsize = 14)
plt.scatter(v[0], v[1], s = 10, c = 'red')
ax.quiver(A[0], A[1], A[2], A[3], angles= 'xy', scale_units = 'xy', color = 'r', scale = 1)
ax.set_xlim([0,10])
ax.set_ylim([0,10])
plt.title('Vector')

plt.grid()
plt.draw()
plt.show()

