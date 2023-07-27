import numpy as np
import matplotlib.pyplot as plt

# v = (5*x) + (7*y)
# negative vector: -v
# multiplying vector with scalar
# base vector: v / (magnitude), labelled i and j

v = [5,7]

def negative_vector(n):
    return -n

def scalar_multiplication(x, y, t):
    new_x = t*x
    new_y = t*y
    return [new_x,new_y]

def magnitude(origin, point):
    x1, y1 = origin
    x2, y2 = point
    x_length = x2 - x1
    y_length = y2 - y1
    mag = int(((x_length)**2 + (y_length)**2)**(1/2))
    return mag

def base_vector(x, y, length):
    length = magnitude([0, 0], [v[0], v[1]])
    i = x/length
    j = y/length
    return [i, j]

A = np.array([[0, 0, v[0], v[1]], [0, 0, negative_vector(v[0]), negative_vector(v[1])]])

plt.figure()
plt.ylabel('y-axis')
plt.xlabel('x-axis')
ax = plt.gca()  # axes is equal to get current axes
ax.annotate(f'v({v[0]}, {v[1]})', (v[0], v[1]), fontsize = 14)
ax.annotate(f'-v({A[1][2]}, {A[1][3]})', (A[1][2], A[1][3]), fontsize = 14)
plt.scatter(v[0], v[1], s = 10, c = 'red')
ax.quiver(A[0][0], A[0][1], A[0][2], A[0][3], angles= 'xy', scale_units = 'xy', color = 'r', scale = 1)
ax.quiver(A[1][0], A[1][1], A[1][2], A[1][3], angles= 'xy', scale_units = 'xy', color = 'b', scale = 1)
ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
plt.axvline(0, c = 'black', ls = '--')
plt.axhline(0, c = 'black', ls = '--')
plt.title('Vector')

plt.grid()
plt.draw()
plt.show()

