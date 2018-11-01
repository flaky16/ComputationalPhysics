# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:12:47 2018

@author: fsk16

Computational Physics Assignment Random Numbers
"""
import random
import pylab as pl
import numpy as np
#y = []
#for x in range(10000):
#    y.append(random.randint(0,100000)*0.00001)
    
#print(np.histogram(y , 10))
#pl.hist(y , 50)
random_no_list = []
y = []
x_min = 0
x_max = 1
def sin_pdf_random(N):
    """ generates N number of random numbers distributed according to pdf P(n) = 1/2 sin(n) """
    return 0


for x in range(10000):
    #print(int(x_max*100000))
    random_no = random.randint(int(x_min*100000) ,  int(x_max*100000)) *0.00001     # Random number accurate to 5 decimals
    random_no_list.append(random_no)
    random_sin_dist_no = np.arccos(1-2*random_no)      # Uniformly generated random number mapped to have a pdf 1/2sinx
    random_sin_dist_no_list.append(random_sin_dist_no)      # Adding random numbers with pdf 1/2sinx to the list for hist
    

pl.figure(1)
pl.hist(y , 100 , alpha = 0.7)
#pl.scatter(t , 2/np.pi * np.sin(t)**2 , c='r')
t = np.linspace(0,np.pi, 10000)
pl.scatter(t , np.sin(t)*1550 , s = 0.5 , c='r')
#pl.hist(random_no_list , 100)
pl.figure(2)
pl.hist(random_no_list , 50)



pl.figure(3)                        # Comparison function
t = np.linspace(-1,1, 100)
pl.scatter(t , 2/np.pi * np.sin(t)**2 , c='r')
pl.scatter(t , 2/np.pi * np.sin(t))
#pl.scatter(t , np.arccos(2*t))
