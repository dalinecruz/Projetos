# -*- coding: iso-8859-1 -*-
'''
Created on 26 de abr. de 2022
Lista1 - Exercício7
@author: daline
'''

def pesquisaValor (dic, chave):
    i = 0
    valores = list(dic.values())
    chaves = list(dic.keys())
   
    while i < len(dic):
        valor = 0
        if chaves[i] == chave:
            #print(i)
            #print(chaves[i])
            valor = valores[i]
            return valor
        i += 1
    else:
        return None

dic = {'Ana':10,'Beto':25, 'Carlos':31, 'Daiana':45, 'Eric':5, 'Marcia':57, 'Enzo':16}

chave = input('Qual item deseja pesquisar? ')

print('O valor pesquisado é: ',pesquisaValor(dic, chave))