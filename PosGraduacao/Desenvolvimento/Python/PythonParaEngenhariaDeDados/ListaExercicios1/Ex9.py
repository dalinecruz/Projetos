# -*- coding: iso-8859-1 -*-
'''
Created on 26 de abr. de 2022
Lista1 - Exercício9
@author: daline
'''

def procuraValor (dic, chave):
    if dic[chave]:
        print('O valor correspondente à chave é:', dic.get(chave))
    else:
        print('A chave não existe no dicionário!')

dic = {'a':1,'b':2, 'c':3, 'd':4, 'e':5}

chave = (input('Insira a chave desejada: '))
procuraValor(dic, chave)