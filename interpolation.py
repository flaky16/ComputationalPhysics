# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:46:55 2018

@author: fsk16

Computational Physics Assignment Interpolation

"""

import numpy as np
import pylab as pl


def linearInterpolation(x , data_X , data_Y):
    """ inputs x, X and Y 1D arrays, X and Y are the data points to be interpolated over given x
        Set X and Y so that X points are in increasing order """
    N = data_X.size                     # Number of data points
    f_x = np.zeros(x.size)
    for k in range(x.size):             # Going through each x position in input x array to find f(x)
        for i in range(N):              # Going through each data points
            if x[k] < data_X[i]:
                f_x [k] =  ((data_X[i] - x[k]) * data_Y[i-1] +  (x[k] - data_X[i-1]) *data_Y[i]) / ( data_X[i] - data_X[i-1])         # f(x) for each k , k is elements in x
                break                    # For loop ends
    return f_x                           # return f(x) as an array in inceasing x

def cubicInterpolation(x , X ,Y):
    return 0


if __name__ == "__main__":
    
    table_x = np.array([-2.1 , -1.45 , -1.3 , -0.2 , 0.1 , 0.15 , 0.8 , 
                    1.1 , 1.5 , 2.8 , 3.8])
    
    table_y = np.array([0.012155, 0.122151,0.184520,0.960789,0.990050,0.977751, 0.527292, 
           0.298197, 0.105399, 3.936690e-4 , 5.355348e-7])

    pl.scatter(table_x , table_y, s=50)
    interp_x = np.linspace(-3 , 3.9, 300)
    pl.plot(interp_x, linearInterpolation(interp_x , table_x , table_y))
