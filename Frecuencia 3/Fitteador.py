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

with np.load('Ensayo 1 CH1_acond.npz') as archivo:
    time_V1 = archivo['x']
    V1 = archivo['y']


# La primer parte de la adquisición tiene errores que debo quitar. Encontré que a partir del punto 1200 no tiene errores el array.    

# Redefino los arrays sacando la primer parte

plt.plot(time_V1, V1,'b-', label = 'datos' )

popt, pcov = curve_fit(seno, time_V1, V1, bounds= ((-np.inf,0.,-np.inf,-5.), (np.inf,np.inf,np.inf,5.)) )
#bounds= ((0,10), (0,np.inf), (-np.inf,np.inf), (-5,5)) )

print (popt)

plt.plot( time_V1, V1,'b*', label = 'datos' )

plt.plot(time_V1, seno(time_V1, *popt), 'r-') #,label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.title( 'Time domain data. V1.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()