import numpy as np
from scipy import integrate


'''Collection of the various IMF functions for stars and SMBHs as
well as the necessary functions to generate the populations'''

### Stars



### SMBH



### Synthesizing population

def F_inv(xs, func, ymax = 1):
    #TODO: Fix docstring to be more accurate and descriptive
    '''Takes X~Unif(0,1) and returns redshift value
    in (0, zmax)
    Inverse of the integral of the IMF, returns y (m, z, etc.)'''

    y_range = np.linspace(0, ymax, 1001, endpoint=True)
    ys = func(y_range)
    F_x = integrate.cumtrapz(ys, y_range, initial=0)

    return np.interp(xs, F_x/(F_x[-1]), y_range)



def generate_zs(n, zmax=1):
    '''Generates n random zs according to the function func
    in F_inv'''
    x = np.random.rand(n)
    return F_inv(x, zmax=zmax)

