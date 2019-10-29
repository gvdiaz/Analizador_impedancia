# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 06:24:40 2019

Objetivo: Tomar las señales recortadas, en un período, y dadas vueltas para realizar el Fitteo. Luego exporta los valores de la función seno.

@author: tanita
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt

def seno(x,a,f,fase,Vbias):
    return ((a*np.sin((2*np.pi*f*x)+fase))+Vbias)
    
def guardar_datos( time_V, a_V, f_V, fase_V, V_bias_V, title=None ):
    """Create a file with data."""
    title = title + '.npz'
    times = time_V
    np.savez( title, x=times, y = ( a_V, f_V, fase_V, V_bias_V))

with np.load('Ensayo 1 CH1_acond.npz') as archivo_1:
    time_V1 = archivo_1['x']
    V1 = archivo_1['y'] 

with np.load('Ensayo 1 CH2_acond.npz') as archivo_2:
    time_V2 = archivo_2['x']
    V2 = archivo_2['y']

# plt.plot(time_V1, V1,'b-', label = 'datos' )

popt_1, pcov_1 = curve_fit(seno, time_V1, V1, bounds= ((-np.inf,0.,-np.inf,-5.), (np.inf,np.inf,np.inf,5.)) )
#bounds= ((0,10), (0,np.inf), (-np.inf,np.inf), (-5,5)) )

print (popt_1)

popt_2, pcov_2 = curve_fit( seno, time_V2, V2, bounds= (( -np.inf, 0., -np.inf, -5.), ( np.inf, np.inf, np.inf, 5.)) )

print (popt_2)

guardar_datos( time_V1, popt_1[0], popt_1[1], popt_1[2], popt_1[3] , 'Ensayo 1 CH1_acond_fit')

guardar_datos( time_V2, popt_2[0], popt_2[1], popt_2[2], popt_2[3] , 'Ensayo 1 CH2_acond_fit')

"""plt.plot( time_V1, seno(time_V1, *popt_1),'b-', label = 'datos' )

plt.plot( time_V2, seno(time_V2, *popt_2), 'r-') #,label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.title( 'Time domain data. V1.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()"""