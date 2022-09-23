######
# create_bins module
# the functions in this module generate bin edges and content based on the given parameters and function


import numpy as np
from math import floor

######
# bins_constant size (cs): outputs a histogram with the bin content and edges with constant sized bins
# in a numpy.histogram format. First and last bins may not have a width = bin_size
# lightcurve: Data used, must be ordered and formated as a numpy array with one axis
# offset: offset in time units of the first edge, used in variance reduction
# bin_size: size of the bins
######

def bins_cs(lightcurve, offset, bin_size):
    if offset != 0:
        hist = np.histogram(lightcurve, np.append(lightcurve[0], np.append(
            np.arange(lightcurve[0] + offset, lightcurve[-1], bin_size), lightcurve[-1])))
    else:
        hist = np.histogram(lightcurve, np.append(
            np.arange(lightcurve[0], lightcurve[-1], bin_size), lightcurve[-1]))
    return hist



######
# bins_constant content (cc): outputs a histogram with the bin content and edges that contain the same content
# in a numpy.histogram format.
# lightcurve: Data used, must be ordered and formated as a numpy array with one axis
# offset: offset in number of events of the first edge, used in variance reduction
# bin_size: size of the bins
######

def bins_cc(lightcurve, offset, bin_num):
    N = len(lightcurve)
    n = N/bin_num
    i = 1
    edges = []
    edges.append(lightcurve[0])
    if offset == 0:
        while floor(n*(i+1)) < N:
            edges.append(lightcurve[floor(n*i)])
            i += 1
    else:
        while floor(n*(i+1)+offset) < N:
            edges.append(lightcurve[floor(n*i+offset)])
            i += 1
    edges.append(lightcurve[-1])
    return np.histogram(lightcurve, edges)



