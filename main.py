# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:55:30 2018

@author: fsk16
"""

import matrixMethods as p

aMatrix = np.array( [[ 2., 1., 9.] ,
                         [-3., 0.,-2.] ,
                         [ 1., 3.,-5.] ] )
    
bVector = np.array( [ -6., 3., 1.] )

x_result = p.GaussJordan( aMatrix, bVector)