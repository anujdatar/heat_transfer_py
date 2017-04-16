"""finite difference tests in python

Author: anuj.datar@gmail
Created: 4/15/2017
"""

# importing standard libraries
import time
import math
import numpy as np

import matplotlib
matplotlib.use('Agg') # enables backend plotting, on headless devices,
## device w/o display - eg. ssh can also use GTK or GTKAgg
## - but need the python Gtk package installed
import matplotlib.pyplot as plt

PI = math.pi
### define material properties
C_P = 564 # heat capacity (J/kgK)
K = 6 # thermal conductivity (W/mK)
RHO = 4450 # material density (kg/m^3)
T_MELT = 1933 # melting point of material (K)
ABS = 0.2 # material absorptivity to laser radiation = 1-Reflectivity
alpha = K/(RHO*C_P) # thermal diffusivity (m^2/s)

### define process properties
L_POW = 100 # laser power (W)
L_VEL = 5e-3 # laser scanning velocity (m/s)
L_SPOT_SIZE = 50e-5 # laser spot size -> diameter (m)
T_INF = 600 # ambient temperature of enclosure (K)
q_laser = ABS * L_POW / (L_SPOT_SIZE**2)

### grid definition
x = 50 # grid spaces in X
y = 10 # grid spaces in Y
z = 3 # grid spaces in Z
bdry_offset = 2 # extra nodes in X & Y to overcome boundary issues and discontinuity
lx = 5e-3 # length of slab in the X-direction
ly = 1e-3 # length of slab in the Y-direction
#lz = 2e-4 ## thickness of slab in the Z-direction

### grid definition
dx = lx/x # grid spacing size in X
dy = ly/y # grid spacing size in Y
dz = dx # grid spacing size in Z
dt = dx/L_VEL # time increment

nx = x + 1 + bdry_offset
ny = y + 1 + bdry_offset
nz = z

Temp = np.zeros((ny, nx)) + T_INF
Temp_old = np.copy(Temp)
