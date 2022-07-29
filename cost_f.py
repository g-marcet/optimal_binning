#######
#This module computes the cost function for a given histogram
#lightcurve: Data used, must be ordered and formated as a numpy array with one axis
#hist: bin content and edges formated as numpy.histogram
# Despite only having one function, this is formated as a module for expandability purposes
#######

def cost_f(lightcurve, hist):
    c = 0.0
    N = len(lightcurve)
    T = lightcurve[-1] - lightcurve[0]

    bin_num = len(hist[0])

    for i in range(0, bin_num):

        c += ((2*hist[0][i])/T)/(hist[1][(i+1)]-hist[1][i])-((hist[1][(i+1)] -
                hist[1][i])/(T))*((hist[0][i]/(hist[1][(i+1)]-hist[1][i]))-(N/T))**2
    return c

