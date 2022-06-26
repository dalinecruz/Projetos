# -*- coding: iso-8859-1 -*-
'''
Created on 26 de abr. de 2022
Lista1 - Exercício10
@author: daline
'''

def maior18 (dic, novoDic):
    i = 0
    valores = list(dic.values())
    chaves = list(dic.keys())
   
    while i < len(dic):
        valor = 0
        chave = ''
        if valores[i] > 18:
            #print(i)
            valor = valores[i]
            chave = chaves[i]
            #print(valor)
            novoDic.update({chave:valor})
        i += 1
    else:
        return novoDic

dic = {'Ana':10,'Beto':25, 'Carlos':31, 'Daiana':45, 'Eric':5, 'Marcia':57, 'Enzo':16}
novoDic = {}

print(maior18(dic, novoDic))
