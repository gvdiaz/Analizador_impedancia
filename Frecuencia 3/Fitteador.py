# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 06:24:40 2019

@author: tanita
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt

def seno(x,a,f,fase,Vbias):
    return ((a*np.sin((2*np.pi*f*x)+fase))+Vbias)

with np.load('Ensayo 1 CH1.npz') as archivo:
    time_V1 = archivo['x']
    V1 = archivo['y']


# La primer parte de la adquisición tiene errores que debo quitar. Encontré que a partir del punto 1200 no tiene errores el array.    

# Redefino los arrays sacando la primer parte

ini_cut = np.empty(1)

ini_cut = 1200

fin_cut = np.empty(1)

fin_cut = ini_cut + 120000

print fin_cut,ini_cut

V = V1[ ini_cut: fin_cut]
time = time_V1[ ini_cut: fin_cut ]

plt.plot(time, V,'b-', label = 'datos' )

popt, pcov = curve_fit(seno, time, V )

print (popt)

plt.plot( time, V,'b*', label = 'datos' )

plt.plot(time, seno(time, *popt), 'r-') #,label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.title( 'Time domain data. V1.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()