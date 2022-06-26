# -*- coding: iso-8859-1 -*-
'''
Created on 7 de jun. de 2022

@author: daline
'''
import pandas as pd

notas = pd.Series([2,7,5,10,6], index=["Wilfred", "Abbie", "Harry", "Julia", "Carrie"])

print(notas)

print("Média:", notas.mean())

print("Desvio padrão:", notas.std())
