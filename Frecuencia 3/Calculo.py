# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 05:59:30 2019

Objetivo: Calcular valor de impedancia medida a partir de los datos acondicionados y fitteados.

@author: tanita
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt
import math

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

"""plt.plot( time_V1, V_Raux, 'b-' ) #V_bias_1),'b-', label = 'datos' )

plt.plot( time_V2, seno(time_V2, amplitud_2, frecuencia_2, fase_2, 0.), 'r-' )

plt.title( 'Time domain data. V_Raux y Vzs1.' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.show() """

""" Cálculo de diferencia de fase entre V_Raux y Vzs1 (V2) """

""" 1ro Detecto cruce positivo de V_Raux """

signo_V_Raux = np.sign(V_Raux)
signo_V_Zs1  = np.sign(V_Zs1)

""" Cálculo de máximo tiempo de fase (el máximo tiempo es +/-pi/2) """
max_fase = (np.pi/2)*(np.power(frecuencia_1,-1))/(2*np.pi)

print signo_V_Raux[1],signo_V_Raux[2]
print (signo_V_Raux[1] != signo_V_Raux[2])

"""
Búsqueda de transiciones positivas y negativas
"""
# Cantidad de veces que se cruza el cero
n1 = math.floor ( np.max( time_V1 ) * frecuencia_1 )
n2 = math.floor ( np.max( time_V2 ) * frecuencia_2 )


cruce_pos_V_Raux = np.zeros( n1 )
cruce_neg_V_Raux = np.zeros( n1 )
cruce_pos_V_Zs1  = np.zeros( n2 )
cruce_neg_V_Zs1  = np.zeros( n2 )

for i in range( 0, V_Raux.size-1):
    
    if signo_V_Raux[i] > signo_V_Raux[i+1]:
        
        cruce_neg_V_Raux = time_V1[i]
        
    elif signo_V_Raux[i] < signo_V_Raux[i+1]:
        
        cruce_pos_V_Raux = time_V1[i]
    
    if signo_V_Zs1[i] > signo_V_Zs1[i+1]:
        
        cruce_neg_V_Zs1 = time_V2[i]
        
    elif signo_V_Zs1[i] < signo_V_Zs1[i+1]:
        
        cruce_pos_V_Zs1 = time_V2[i]

""" Cálculo de diferencia de fase entre señales tomando como referencia V_Raux"""
# Pasaje de tiempos a grados

cruce_pos_V_Raux_grados = cruce_pos_V_Raux*(360)*frecuencia_1
cruce_neg_V_Raux_grados = cruce_neg_V_Raux*(360)*frecuencia_1
cruce_pos_V_Zs1_grados  = cruce_pos_V_Zs1*(360)*frecuencia_2
cruce_neg_V_Zs1_grados  = cruce_neg_V_Zs1*(360)*frecuencia_2
"""
print 'Cruce negativo V_Raux',cruce_neg_V_Raux_grados
print 'Cruce negativo V_Zs1 ',cruce_neg_V_Zs1_grados
print 'Cruce positivo V_Raux',cruce_pos_V_Raux_grados
print 'Cruce positivo V_Zs1 ',cruce_pos_V_Zs1_grados
"""
diff_fase_V_Raux_to_V_Zs1_neg = cruce_neg_V_Raux_grados - cruce_neg_V_Zs1_grados
diff_fase_V_Raux_to_V_Zs1_pos = cruce_pos_V_Raux_grados - cruce_pos_V_Zs1_grados

print 'Desfasaje de V_Raux  V_Zs1 negativo',-diff_fase_V_Raux_to_V_Zs1_neg
print 'Desfasaje de V_Raux  V_Zs1 positivo',-diff_fase_V_Raux_to_V_Zs1_pos

""" Cálculo de impedancia """

modulo_Zs1 = 15e3*np.max(V_Zs1)/np.max(V_Raux)
fase_Zs1 = -diff_fase_V_Raux_to_V_Zs1_neg
capacidad = np.power(modulo_Zs1*2*np.pi*frecuencia_1,-1)

print 'Módulo de Zs1',modulo_Zs1
print 'Fase de Zs1',fase_Zs1
print 'Frecuencia ensayo',frecuencia_1
print 'Supuesto valor de capacidad',capacidad

plt.figure()

plt.plot( time_V2, signo_V_Zs1 , 'r-')
plt.plot( time_V1, signo_V_Raux, 'b-')

plt.title( 'Time domain data. Cambio signo V_Raux (azul) y V_zs1 (roja)' )
plt.xlabel( 'Time (s)' )
plt.ylabel( 'Volts' )
plt.grid( True )
plt.ylim(top=1.5)  # adjust the top leaving bottom unchanged
plt.ylim(bottom=-1.5)  # adjust the bottom leaving top unchanged
plt.show()