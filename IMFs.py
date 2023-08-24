import numpy as np
from scipy import integrate


'''Collection of the various IMF functions for stars and SMBHs as
well as the necessary functions to generate the populations. Running
this file alone will plot all IMFs and a normalized random sampling
of each to demonstrate agreement.'''

### Stars

# saltpeter power law (0.1 to 100M_sun)
def salpeter(m, alpha=2.35):
    '''Standard Salpeter IMF'''
    # https://articles.adsabs.harvard.edu/pdf/1955ApJ...121..161S

    return m**-alpha

def kroupa(m, alpha_low=1.3, alpha_high=2.3):
    '''Kroupa IMF: like a Salpeter IMF but scales differently for
       m<0.5'''
    # https://ui.adsabs.harvard.edu/abs/2001MNRAS.322..231K/abstract
    return

# chabrier
def chabrier(m, low=0.01, high=100):
    # https://iopscience.iop.org/article/10.1086/376392/pdf

    return


### SMBH

def log_flat(m, low=6, high=8):
    '''A flat IMF in log space, between 10^low and 10^high'''

    return

#find ones in Bricman

#Ask Zach for favorite IMFs


### Synthesizing population

def F_inv(xs, func, ymax = 1):
    #TODO: Fix docstring to be more accurate and descriptive
    '''Takes X~Unif(0,1) and returns y value in (0, ymax)
    Inverse of the integral of the IMF, returns y (m, z, etc.).'''

    y_range = np.linspace(0, ymax, 1001, endpoint=True) 
    ys = func(y_range)
    F_x = integrate.cumtrapz(ys, y_range, initial=0)

    return np.interp(xs, F_x/(F_x[-1]), y_range)



def generate_ys(n, func, zmax=1):
    '''Generates n random zs according to the function func
    in F_inv'''
    x = np.random.rand(n)
    return F_inv(x, func, zmax=zmax)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    star_IMFs = [salpeter, chabrier] #put all IMFs for stars in here
    smbh_IMFs = [] #same, but for SMBHs

    # make 2-row fig that can hold all IMFs above (stars on top, smbh on bottom)
    # fig, axs = plt.subplots(nrows=2, ncols=max(len(star_IMFs), len(smbh_IMFs)))

    for i, func in enumerate(star_IMFs):
        pass

    for i, func in enumerate(smbh_IMFs):
        pass