# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:57:25 2018

@author: fsk16
"""

import numpy as np
import matplotlib.pylab as pl
n = 30                        # No of data points
rangeMin = -5                   # Range of function and polynomial
rangeMax = 5


def LagrangePolynomial( k ):   # Inputs arrays
    """ Implements Lagrange Polynomial from the equation directly
        arrays for data points x and f_x have to be defined 
        n , number of data points, have to be defined, too
    """
    assert len(x) == len(f_x) , " x and f not same size "
    sum_ = 0
    for i in  range( n ):
        product = 1             # Reset the product for each i
        for j in  range( len(x) ):
            if i!=j:
                product = product * ( k - x[j] ) / ( x[i] - x[j] )  # Product over j's for a given i
        sum_ = sum_ + product * f_x[i]              # Sum over i's after product over j done
    return sum_

if __name__ == "__main__":

    x = np.linspace(rangeMin , rangeMax , n)     # Array for x values 

    # Different f_x to try:

    f_x = np.zeros(n)
    for n in range( len(x) ):
        f_x[n] = np.cos( x[n] )               # Create array of f(x)

    pl.scatter( x, f_x )


    # Plot Polynomial

    X = np.linspace( -5, 5, 1000)
    pl.scatter(X , LagrangePolynomial(X) , s=2)
    pl.xlabel("x")
    pl.ylabel("f_x")
    pl.axis([4.6,5.2,-0.5,0.5])
    #pl.savefig("LagrangePolyN=20")

