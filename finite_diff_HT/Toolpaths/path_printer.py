"""Toolpath selector

Author: anuj.dater@gmail.com
Created: 4/15/2017
"""

import numpy as np
import matplotlib.pyplot as plt

from finite_diff_HT.finite_diff_HT.Toolpaths import raster_path
#from raster import raster_path

x = 5
y = 5

shader = np.zeros((y, x))

path = raster_path(x, y)
print(path)

for i in range(x*y):
    shader[int(path[i, 0]), int(path[i, 1])] = path[i, 2]

plt.contourf(shader)
plt.jet()
plt.savefig('img.jpg')
