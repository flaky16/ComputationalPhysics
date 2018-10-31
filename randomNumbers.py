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
x_max = np.pi
for x in range(30000):
    random_no = random.randint(int(x_min*100000) , int(x_max*100000)) *0.00001
    random_no_list.append(random_no)
    #y.append(1/2*np.sin(random_no))
    y.append(2/np.pi * np.sin(random_no)**2)
    
#print(np.histogram(y , 10))
pl.figure(1)
pl.hist(y , 100)
#pl.hist(random_no_list , 100)
pl.figure(2)
pl.hist(random_no_list , 50)



pl.figure(3)                        # Comparison function
t = np.linspace(0,np.pi, 100)
pl.scatter(t , 2/np.pi * np.sin(t)**2 , c='r')
pl.scatter(t , 2/np.pi * np.sin(t))