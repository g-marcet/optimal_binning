#######
# plots module
# all functions that plot are defined in this module
#######


import matplotlib.pyplot as plt
import numpy as np

##### Only a plot, costs must be computed beforehand! This is done in the optimal_bin.py script
#Plots the cost function over bin size
#cost is a list with the values of the cost function
#bin_range is the range of bin width used
#####

def draw_cost_cs(cost, bin_range):

    plt.plot(np.arange(bin_range[0], bin_range[1], bin_range[2]), cost, '.k', label='Cost function')
    plt.xlabel('bin width [s]')
    plt.ylabel('Cost function')
    plt.xscale('log')
    plt.show()

##### Only a plot, costs must be computed beforehand! This is done in the optimal_bin.py script
#Plots the cost function over bin content
#cost is a list with the values of the cost function
#content is the range of bin content used
#####

def draw_cost_cc(cost, content):

    plt.plot(content, cost, '.k', label='Cost function')
    plt.xlabel('Content per')
    plt.ylabel('Cost function')
    plt.xscale('log')
    plt.show()

#####
#Plots a histogram for given bin contents and its corresponding edges (see numpy.histogram)
#bins: bin content and edges formated as numpy.histogram
#####

def draw_hist(bins):

    x = []
    xerr = []
    for k in range(len(bins[0])):
        x.append((bins[1][k+1]+bins[1][k])*0.5)
        xerr.append((bins[1][k+1]-bins[1][k]))
    plt.errorbar(x, np.divide(bins[0], xerr), xerr=np.multiply(xerr,0.5),
             yerr=np.divide(np.sqrt(bins[0]), xerr), c='grey', ls='', marker=',')
    plt.ylabel('Events [ph s$^{-1}$]')
    plt.xlabel('Time [s]')
    plt.show()

