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

def cubicInterpolation(x , data_x ,data_f):
    # Setting Matrices and vectors
    N = data_x.size - 1                               # Number of data points, - 1 for indexing
    matrix_X = np.zeros([N-1,N-1])                    # Initializing the matrix and vectors in the equation to be solved
    vector_f = np.zeros([N-1])

    matrix_X[0][0]     = (data_x[2] - data_x[0]) / 3                                        # Setting first row before loop
    matrix_X[0][1]     = (data_x[2] - data_x[1]) / 6            
    matrix_X[N-2][N-3] = (data_x[N-1] - data_x[N-2]) / 6                                    # Setting last row before loop
    matrix_X[N-2][N-2] = (data_x[N]   - data_x[N-2]) / 3 
    
    vector_f[0] = ( (data_f[2] - data_f[1]) / ( data_x[2] - data_x[1] )                     # Setting first element
                  - (data_f[1] - data_f[0]) / ( data_x[1] - data_x[0] ) )
    
    vector_f[N-2] = ( (data_f[N] - data_f[N-1]) / ( data_x[N]  -  data_x[N-1] )             # Setting last element
                  - (data_f[N-1] - data_f[N-2]) / ( data_x[N-1] - data_x[N-2] ) )
    
    for row in np.arange(1,N-2):                                                            # Filling matrix and vector row by row
        matrix_X[row][row-1] = (data_x[row+1] - data_x[row]) / 6                            # First matrix element in row
        matrix_X[row][row] = (data_x[row+2] - data_x[row]) / 3                              # Second matrix element in row
        matrix_X[row][row+1] = (data_x[row+2] - data_x[row+1]) / 6                          # Last matrix element in row
        vector_f[row] = ( (data_f[row+2] - data_f[row+1]) / ( data_x[row+2] - data_x[row+1] )
                          - (data_f[row+1] - data_f[row]) / ( data_x[row+1] - data_x[row] ) )     # Right hand side of eqn
    
    # Here the matrix X and vector f in X f'' = f eqn are ready to find f'' 
    vector_ddf = np.zeros(N+1)
    ddf_withoutBC = lu.solveEquation(matrix_X , vector_f)                       # Imported function solves eqn for f'' excluding natural spline BC's
    for i in range(N-1):
        vector_ddf[i+1] = ddf_withoutBC[i]                                      # Adding natural spline BC to f'' vector

    # Calculating f(x) from given equation for an input array of x's
    cubic = np.zeros(x.size)
    for k in range(x.size):                                                     # Going through each x position in input x array to find f(x)
        for i in np.arange(1, N+1):                                             # Going through data points
            if x[k] < data_x[i]:
                A = ( data_x[i] - x[k] ) / ( data_x[i] - data_x[i-1] )
                B = 1 - A
                C = (A**3 - A ) * (data_x[i] - data_x[i-1])**2 / 6
                D = (B**3 - B ) * (data_x[i] - data_x[i-1])**2 / 6

                cubic[k] = A * data_f[i-1] + B * data_f[i] + C * vector_ddf[i-1] + D * vector_ddf[i]
                break
    return cubic

if __name__ == "__main__":
    
    table_x = np.array([-2.1 , -1.45 , -1.3 , -0.2 , 0.1 , 0.15 , 0.8 , 
                    1.1 , 1.5 , 2.8 , 3.8])
    
    table_y = np.array([0.012155, 0.122151,0.184520,0.960789,0.990050,0.977751, 0.527292, 
           0.298197, 0.105399, 3.936690e-4 , 5.355348e-7])

    pl.scatter(table_x , table_y, s=50)
    interp_x = np.linspace(-2 , 3.8, 300)
    pl.plot(interp_x, cubicInterpolation(interp_x , table_x , table_y))
    #pl.axis([-0.5,1, 0.6 ,1.2])
