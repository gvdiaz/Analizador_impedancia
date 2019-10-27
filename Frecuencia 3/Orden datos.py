# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:59:07 2019

@author: tanita
"""

import numpy as np
import matplotlib.pyplot as plt

with np.load('Ensayo 1 CH1.npz') as archivo:
    time_V1 = archivo['x']
    V1 = archivo['y']

with np.load('Ensayo 1 CH2.npz') as archivo:
    time_V2 = archivo['x']
    V2 = archivo['y']

