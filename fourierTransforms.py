# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 11:57:36 2018

@author: fsk16

Computational Physics Fourier Transforms
"""

import numpy as np
import pylab as pl
from numpy.fft import fft , ifft , fftshift

N = 2**8                                        # Number of samples

def h(T):                                       # The given h step function
    h = np.zeros(T.size)
    for t in range(T.size):
        if T[t] > 3 and T[t] < 5:
             h[t] = 4
        else:
             h[t] = 0           
    return h

def g(t):                                       # The given g Gaussian function
    return 1/np.sqrt(np.pi*2) * np.exp(-t**2 / 2)


t = np.linspace(-8 , 8 , N)             # Time domain
dt = (t[N-1] - t[0]) / N                # Time steps

h = h(t)
g = g(t)
hf = fft(h) * dt                        # Fourier transform of h in given domain t
gf = fft(g) * dt                        # Fourier transform of g in given domain t

hxgf = hf * gf                          # Fourier transform of the convolution using the convolution theorem
hxg = ifft(hxgf) / dt                   # Inverse Fourier transform to get the convolution funcion

hxg = fftshift(hxg)                     # Shift the convoluted function to appropriate position


#tf = np.linspace(0 , 1/dt, N/2)         # Frequency domain


pl.plot(t , hxg)
pl.plot(t , h)
pl.plot(t , g)

pl.xlabel("t")
pl.legend(["(h*g)(t)" , "h(t)" , "g(t)"])
#pl.savefig("convolution.png")
