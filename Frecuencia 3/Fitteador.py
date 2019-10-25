# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 06:24:40 2019

@author: tanita
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt

def seno(x,a,f,fase):
    return (a*np.sin((2*np.pi*f*x)+fase))

with np.load('Ensayo 1 CH1.npz') as archivo:
    time_V1 = archivo['x']
    V1 = archivo['y']


# La primer parte de la adquisición tiene errores que debo quitar. Encontré que a partir del punto 1200 no tiene errores el array.    

# Redefino los arrays sacando la primer parte

ini_cut = np.empty(1)

ini_cut = 1200

print V1.size()

V = V1[ ini_cut: V1.size() ]
time = time_V1[ ini_cut: time_V1.size() ]

plt.plot(time, V,'b*', label = 'datos' )

""" print (V1.shape)

popt, pcov = curve_fit(seno, time_V1, V1 )

print (popt)

plt.plot( time_V1, V1,'b*', label = 'datos' )

plt.plot(time_V1, seno(time_V1, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))



plt.title( 'Time domain data. V1.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()"""