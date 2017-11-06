""" Source matrix for unsteady problem

Author: anuj.datar@gmail.com
Created: 4/18/2017
"""

import numpy as np

def source_time(S_net, theta, coeff_matrix, rho, cp, dt):
    """ source matrix for unsteady problem using Implicit Euler

    Args:

    Returns:
    """
    nx = S_net.shape[1]
    ny = S_net.shape[0]

    Source_time = np.zeros(())