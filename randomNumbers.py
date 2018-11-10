# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:12:47 2018

@author: fsk16

Computational Physics Assignment Random Numbers
"""
import random
import pylab as pl
import numpy as np
import time

def uniform_random(N):
    random_no_list = []
    for x in range(N):
        random_no = random.uniform(0 , 1)               # Generate uniform float between 0 and 1 by built in function
        random_no_list.append(random_no)
    return random_no_list                               # Return a list of N random numbers

def sin_pdf_random(N):
    """ returns a list of N random numbers according to pdf P(n) = 1/2 sin(n) between 0 and pi using transformation method """
    sin_pdf = []
    for x in range(N):
        random_no = random.uniform(0 , 1)               # Uniform random number between 0 , 1 
        sin_random = np.arccos(1-2*random_no)           # Mapping uniformly generated random number to have desired pdf
                                                        # Domain becomes [0,pi]
        sin_pdf.append(sin_random)
    return sin_pdf                                      # Return a list of N random numbers

def sin2_pdf_random(N):
    """ returns a list of N random numbers according to pdf P(n) = 2/pi sin**2(n) between 0 and pi using rejection method """
    accepted = []
    while len(accepted) < N+1:                                  # Loop until N random numbers with desired pdf are generated
        random_no = random.uniform(0 , 1)
        random_no= np.arccos(1-2*random_no)                     # Random number with distribution of normalized comparison function
        random_y = random.uniform(0 ,  comparison(random_no))   # Generating random y between zero and comparison function
        if random_y < 2/np.pi *np.sin(random_no)**2:            # Check if random y is in the area enclosed by desired pdf function
            accepted.append(random_no)
    return accepted                                             # Return a list of N random numbers
         
def comparison(random_no):
    return 2/np.pi * np.sin(random_no)                  # Comparison function for rejection method


if __name__ == "__main__":

    N = 10**5
    random_no_list = uniform_random(N)
    
    start_sin = time.time()
    sin_pdf = sin_pdf_random(N)
    end_sin = time.time()
    
    start_sin2 = time.time()
    sin2_pdf = sin2_pdf_random(N)
    end_sin2 = time.time()
    
    print("Time it takes for pdf = 1/2sin(x): " , end_sin - start_sin)
    print("Time it takes for pdf = 2/pi * sin**2(x): " , end_sin2 - start_sin2)
    print("Time ratio t2/t1 = " , (end_sin2 - start_sin2) / (end_sin - start_sin))
    
    t = np.linspace(0,np.pi, 1000)      # Domain for plotting the functions
    
    pl.figure(1)                        # Uniform distribution
    pl.hist(random_no_list , 50)
    pl.xlabel("x")
    pl.ylabel("number of samples")
    
    
    pl.figure(2)                        # Pdf = 1/2sin(x) distribution 
    pl.hist(sin_pdf , 100 , alpha = 0.5)
    pl.scatter(t , np.sin(t)*1550 , s = 0.5 , c='r')
    pl.xlabel("x")
    pl.ylabel("number of samples")
    
    pl.figure(3)                        # Pdf = 2/pi sin**2(x) distribution
    pl.hist(sin2_pdf , 100 , alpha = 0.7)
    pl.scatter(t , np.sin(t)**2*1950 , s = 0.5 , c='r')
    pl.scatter(t , np.sin(t)*1950 , s = 0.5 , c='r')
    pl.xlabel("x")
    pl.ylabel("number of samples")
    
    pl.figure(4)                        # Comparison function
    pl.scatter(t , 2/np.pi * np.sin(t)**2 , c='r')
    pl.scatter(t , 2/np.pi * np.sin(t))
    
