import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
vertices = np.array([
    [0, -6.206, -3],
    [3.125, -5.375, -3],
    [5.375, -3.125, -3],
    [6.206, 0, -3],
    [5.375, 3.125, -3],
    [3.125, 5.375, -3],
    [0, 6.206, -3],
    [-3.125, 5.375, -3],
    [-5.375, 3.125, -3],
    [-6.206, 0, -3],
    [-5.375, -3.125, -3],
    [-3.125, -5.375, -3],
    [0, 0, 7]])

faces = np.array([
    [0, 1, 12],
    [1, 2, 12],
    [2, 3, 12],
    [3, 4, 12],
    [4, 5, 12],
    [5, 6, 12],
    [6, 7, 12],
    [7, 8, 12],
    [8, 9, 12],
    [9, 10, 12],
    [10, 11, 12],
    [11, 0, 12]])

base = np.array([
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])

figure = [Poly3DCollection([vertices[face] for face in faces], alpha=1, facecolor='orange', edgecolor='k')]
# figure.append(Poly3DCollection([vertices[face] for face in base], alpha=1, facecolor='orange', edgecolor='k'))
ax.add_collection3d(figure[0])
# ax.add_collection3d(figure[1])
ax.auto_scale_xyz([-8, 8], [-8, 8], [-8, 8])
plt.show()