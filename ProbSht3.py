# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:30:46 2018

@author: fsk16

Computational Physics Prob Sheet 3
"""

import numpy as np

# 1st question written in Xcode already

# 2nd Question:
def GaussJordan( matrix , vector):
    """ Implements Gauss Jordan Elimination on the arguments
        A and b where Ax = b. x is returned as a vector. 
    """
    assert matrix.shape[1] == vector.size ,"Check dimensions of matrix and vector"  # First check if dimensions correct

    for m in range(matrix.shape[0]):            # Looping through columns m
        assert matrix[m][m] != 0 , "Diagonal term zero, 0/0 error" # Error if diagonal term zero
            
        vector[m] = vector[m] / matrix[m][m]    # Changing vector before changing A_mm
        matrix[m] = matrix[m] / matrix[m][m]    # Setting A_mm = 1
        
        for n in range(matrix.shape[1]):        # Looping through rows for a column m
            if n!=m:                            # Making sure we dont change A_mm
                
                vector[n] = vector[m] * -matrix[n][m] + vector[n]       # V_n = V_n + V_m * A_nm
                matrix[n] = matrix[m] * -matrix[n][m] + matrix[n]       # A_mn = 0
                    
    print("The result is: ", vector)
    return vector        # Going to return the resulting vector b, which is also x
    

""" Function gives correct values, except for diagonal terms being zero, at which gives an error """
if __name__ == "__main__":
    
    aMatrix = np.array( [[ 2., 1., 9.] ,
                         [-3., 0.,-2.] ,
                         [ 1., 3.,-5.] ] )
    
    bVector = np.array( [ -6., 3., 1.] )

    x_result = GaussJordan( aMatrix, bVector)
