# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 11:57:36 2018

@author: fsk16

Computational Physics Fourier Transforms
"""

import numpy as np
import pylab as pl
from numpy.fft import fft , fftfreq

N=2**12
x = np.linspace(-6,6,N)
fftdom = np.linspace(0,6,N)
#t = np.linspace(-6,6,32)
w = 4
y = np.exp(-(x)**2/(w*w))/np.sqrt(2*np.pi*(w*w))

f = np.sin(w*x)
fftresult = fft(f) / np.sqrt(N)
print(f, fftresult)
pl.plot()
pl.scatter(x , f)
pl.scatter(x , fftresult)
#pl.axis([-6,6,-1,110])
#t = np.arange(256)
#sp = np.fft.fft(np.exp(-(x)**2/(w*w))/np.sqrt(2*np.pi*(w*w)))
#freq = fftfreq(x.shape[-1])
#pl.plot(freq, sp.real, freq, sp.imag)
#pl.scatter(x, sp.real)





"""
def DFT(f , x):
    N = f.size
    F_x = 0
    for n in range(N-1):
        F_x += f[n]*np.exp(1j*2*np.pi*x*n/N)
    return F_x

def inv_DFT(F , x):
    N = F.size
    f_x = 0
    for n in range(N-1):
        f_x += F[n]*np.exp(-1j*2*np.pi*x*n/N)/N
    return f_x

#Y = DFT(y ,x)
#pl.scatter(x , DFT(y,x))

#print(Y)
#pl.scatter(x , inv_DFT(Y,x))
#pl.axis([-4,4,-1,1])
    """