# -*- coding: iso-8859-1 -*-
'''
Created on 31 de mai. de 2022

@author: daline
'''
import numpy as np

x = np.array([4, 3, 7, -9, 1])
print(x)
print("Tipo :" + str(x.dtype))
print(x.itemsize)# tamanho em bytes de cada elemento (int32)
print(x.size)# número de elementos em x
print(x.itemsize * x.size)# tamanhode x em bytes
print(x.nbytes)# idemacima
print(x.ndim)# número de dimensões (1: array, 2: matriz, etc. )
a= np.arange(15).reshape(3,5)
print(a)
print(a.shape)
