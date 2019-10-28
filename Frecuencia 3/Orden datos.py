# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:59:07 2019

@author: tanita
"""

import numpy as np
import matplotlib.pyplot as plt

def guardar_plot( tension, tiempo, title=None ):
    """Create a file with data."""
    title = title + '.npz'
    np.savez( title, x=tiempo, y=tension)

with np.load('Ensayo 1 CH1.npz') as archivo:
    time_V1 = archivo['x']
    V1 = archivo['y']

with np.load('Ensayo 1 CH2.npz') as archivo:
    time_V2 = archivo['x']
    V2 = archivo['y']

""" Función para dar vuelta datos de las tensiones"""

V1_inv = np.zeros(V1.size)

V2_inv = np.zeros(V2.size)

print V2[V2.size-1]

for i in range(0,(V1.size-1)):
    V1_inv[i] = V1[V1.size-i-1]
    V2_inv[i] = V2[V2.size-i-1]

""" Recortador de la imagen """

ini_cut = np.empty(1)

ini_cut = 0

fin_cut = np.empty(1)

fin_cut = ini_cut + 120000

print fin_cut,ini_cut

V1_inv_cort = V1_inv[ ini_cut: fin_cut]
time_V1_cort = time_V1[ ini_cut: fin_cut ]

V2_inv_cort = V2_inv[ ini_cut: fin_cut]
time_V2_cort = time_V2[ ini_cut: fin_cut ]

guardar_plot(V1_inv_cort,time_V1_cort,'Ensayo 1 CH1_acond')
guardar_plot(V2_inv_cort,time_V2_cort,'Ensayo 1 CH2_acond')

plt.plot(time_V1_cort, V1_inv_cort,'b-', label = 'datos' )

#plt.plot( time_V1, V1,'r-', label = 'datos' )

plt.title( 'Time domain data. V1.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()

plt.figure()
plt.plot(time_V2_cort, V2_inv_cort,'b-', label = 'datos' )

#plt.plot( time_V2, V2,'r-', label = 'datos' )

plt.title( 'Time domain data. V2.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()