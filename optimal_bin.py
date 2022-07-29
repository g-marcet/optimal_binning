
#######
# Main script of the program
# The functions in the script compute the optimal bin distribution for a given method and lightcurve
#######



import create_bins as bin
from cost_f import *
from plots import *
import numpy as np
from math import floor

#########
# Optimal bin constant size (cs): Computes the optimal bin size for a lightcurve assuming all bins have the same size
# lightcurve: Data used, must be ordered and formated as a numpy array with one axis
# bin_range: range of bins studied, must be formated as a 3 item list, [start, end, step] - They do not need to be integers
# times: times that the initial bin size is shifted in order to get rid of variance in the cost function calculation
# draw: True if a plot of the cost function is wanted
#########

def optimal_bin_cs(lightcurve, bin_range = [1,300,1], times=20, draw = True):
    cost = []

    for bin_size in np.arange(bin_range[0], bin_range[1], bin_range[2]):
        c = 0.0
        for i in range(0, times):
            offset = i * bin_size / times
            c += cost_f(lightcurve, bin.bins_cs(lightcurve, offset, bin_size))
        cost.append(c/times)
    opt_width = bin_range[2]*cost.index(min(cost))+bin_range[0]
    print('Optimal bin width: ', opt_width)
    if draw == True:
        draw_cost_cs(cost, bin_range)

    return opt_width


#########
# Optimal bin constant content (cc): Computes the optimal bin size for a lightcurve assuming all bins have the same number of events
# lightcurve: Data used, must be ordered and formated as a numpy array with one axis
# bin_range: range of bins studied, must be formated as a 3 item list, [start, end, step] - They do not need to be integers
# draw: True if a plot of the cost function is wanted
#########

def optimal_bin_cc(lightcurve, bin_range = [1,300,1], draw = True):
    cost = []
    for bin_num in np.arange(bin_range[0], bin_range[1], bin_range[2]):
        c = 0.0
        n = len(lightcurve)/bin_num
        for i in range(floor(n)):
            c += cost_f(lightcurve, bin.bins_cc(lightcurve, i, bin_num))
        cost.append(c/floor(n))
    opt_bin = bin_range[2]*cost.index(min(cost))+bin_range[0]
    print('Optimal bin number: ', opt_bin)
    print('Optimal content per bin: ', len(lightcurve)/opt_bin)
    if draw == True:
        draw_cost_cc(cost, np.divide(len(lightcurve), np.arange(bin_range[0], bin_range[1], bin_range[2])))
    return opt_bin
    

# Define the lightcurve data. It must be formated as a sorted numpy array with one axis
# numpy.loadtxt and numpy.sort might prove useful functions for this purpose

data = #example: np.sort(np.loadtxt('path'))


#Example functions
draw_hist(bin.bins_cs(data, 0)) #Get the optimal bin size and plot the according histogram
draw_hist(bin.bins_cc(data, 0)) #Get the optimal bin content and plot the according histogram
        