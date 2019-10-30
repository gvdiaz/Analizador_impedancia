# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 05:59:30 2019

Objetivo: Calcular valor de impedancia medida a partir de los datos acondicionados y fitteados.

@author: tanita
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt

def seno(x,a,f,fase,Vbias):
    return ((a*np.sin((2*np.pi*f*x)+fase))+Vbias)

with np.load('Ensayo 1 CH1_acond_fit.npz') as archivo_1:
    time_V1 = archivo_1['x']
    sen_param_1 = archivo_1['y'] 

with np.load('Ensayo 1 CH2_acond_fit.npz') as archivo_2:
    time_V2 = archivo_2['x']
    sen_param_2 = archivo_2['y']

amplitud_1 =   sen_param_1[0]
frecuencia_1 = sen_param_1[1]
fase_1 =       sen_param_1[2]
V_bias_1 =     sen_param_1[3]

amplitud_2 =   sen_param_2[0]
frecuencia_2 = sen_param_2[1]
fase_2 =       sen_param_2[2]
V_bias_2 =     sen_param_2[3]

V_Raux = seno(time_V1, amplitud_1, frecuencia_1, fase_1, 0.) - seno(time_V2, amplitud_2, frecuencia_2, fase_2, 0.)

V_Zs1 = seno(time_V2, amplitud_2, frecuencia_2, fase_2, 0.)

plt.plot( time_V1, V_Raux, 'b-' ) #V_bias_1),'b-', label = 'datos' )

plt.plot( time_V2, seno(time_V2, amplitud_2, frecuencia_2, fase_2, 0.), 'r-' ) #V_bias_2), 'r-') 
plt.plot( time_V1, seno(time_V1, amplitud_1, frecuencia_1, fase_1, 0.), 'g-' )

plt.title( 'Time domain data. V1 y V2.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show()

""" Cálculo de diferencia de fase entre V_Raux y Vzs1 (V2) """

""" 1ro Detecto cruce positivo de V_Raux """

signo_V_Raux = np.sign(V_Raux)
signo_V_Zs1  = np.sign(V_Zs1)

plt.figure()

plt.plot(  time_V2, signo_V_Zs1, 'r-')
plt.plot( time_V1, signo_V_Raux, 'b-')

plt.title( 'Time domain data. Cambio signo V_Raux y V_zs1' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.ylim(top=1.5)  # adjust the top leaving bottom unchanged
plt.ylim(bottom=-1.5)  # adjust the bottom leaving top unchanged
plt.show()