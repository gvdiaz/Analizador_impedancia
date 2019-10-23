# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 06:12:27 2019

@author: Negrete
"""
from ctypes import *
from numpy import *
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

#Pruba para extender cadena de caracteres

title = 'Extensión 1'
print title
title = title + 'texto de extensión'
print title

with np.load('Ensayo 1 CH1.npz') as archivo:
    V1 = archivo['x']
    time_V1 = archivo['y']
    
print V1.shape

plt.plot( V1, time_V1 )
plt.title( 'Time domain data. V1.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()

with np.load('Ensayo 1 CH2.npz') as archivo:
    V2 = archivo['x']
    time_V2 = archivo['y']
    
plt.plot( V2, time_V2 )
plt.title( 'Time domain data. V2.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()