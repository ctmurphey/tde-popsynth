import numpy as np
from scipy import integrate


'''Collection of the various IMF functions for stars and SMBHs as
well as the necessary functions to generate the populations. Running
this file alone will plot all IMFs and a normalized random sampling
of each to demonstrate agreement.'''

### Constants:
stars_lower_bound = 0.1 #M_sun
stars_upper_bound = 100
smbh_lower_bound  = int(1e6)
smbh_upper_bound  = int(1e8)



### Stars

# saltpeter power law (0.1 to 100M_sun)
def salpeter(m, alpha=2.35):
    '''Standard Salpeter IMF'''
    # https://articles.adsabs.harvard.edu/pdf/1955ApJ...121..161S

    return m**-alpha

def kroupa(m, alpha_low=1.3, alpha_high=2.3, cutoff=0.5):
    '''Kroupa IMF: like a Salpeter IMF but scales differently for
       m<0.5'''
    # https://ui.adsabs.harvard.edu/abs/2001MNRAS.322..231K/abstract  
    
    return np.array([(x<cutoff)*x**-alpha_low + (x>=cutoff)*x**-alpha_high for x in m])

# chabrier
def chabrier(m):
    # https://iopscience.iop.org/article/10.1086/376392/pdf

    return


### SMBH

def log_flat(m):
    '''A flat IMF in log space'''

    return 

#find ones in Bricman

#Ask Zach for favorite IMFs
def schecter(m):
    '''Schecter IMF'''
    return

### Synthesizing population

def F_inv(xs, func, ymin, ymax):
    #TODO: Fix docstring to be more accurate and descriptive
    '''Takes X~Unif(0,1) and returns y value in (0, ymax)
    Inverse of the integral of the IMF, returns y (m, z, etc.).'''

    y_range = np.linspace(ymin, ymax, 1001, endpoint=True) 
    ys = func(y_range)

    F_x = integrate.cumtrapz(ys, y_range, initial=0)

    return np.interp(xs, F_x/(F_x[-1]), y_range)



def generate_ys(n, func, ymin, ymax):
    '''Generates n random zs according to the function func
    in F_inv'''
    x = np.random.rand(n)
    return F_inv(x, func, ymin=ymin, ymax=ymax)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    star_IMFs = [salpeter, kroupa] #put all IMFs for stars in here
    smbh_IMFs = [log_flat, schecter] #same, but for SMBHs

    # make 2-row fig that can hold all IMFs above (stars on top, smbh on bottom)
    fig, axs = plt.subplots(nrows=2, ncols=max(len(star_IMFs), len(smbh_IMFs)))

    for i, func in enumerate(star_IMFs):
        ys = generate_ys(int(1e5), func, ymin=stars_lower_bound, ymax=stars_upper_bound)
        ms = np.logspace(np.log10(stars_lower_bound), np.log10(stars_upper_bound), 50)

        # Histogram of samples for each IMF
        axs[0, i].hist(ys, bins=ms, density=True)
        # Actual pdf that should trace the histogram
        axs[0, i].loglog(ms, func(ms)/(integrate.trapz(func(ms), ms)))

        axs[0, i].set_title(str(func).split()[1])
        

    for i, func in enumerate(smbh_IMFs):
        pass


plt.show()