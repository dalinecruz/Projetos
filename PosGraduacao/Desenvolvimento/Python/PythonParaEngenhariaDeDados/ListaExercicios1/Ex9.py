# -*- coding: iso-8859-1 -*-
'''
Created on 26 de abr. de 2022
Lista1 - Exerc�cio9
@author: daline
'''

def procuraValor (dic, chave):
    if dic[chave]:
        print('O valor correspondente � chave �:', dic.get(chave))
    else:
        print('A chave n�o existe no dicion�rio!')

dic = {'a':1,'b':2, 'c':3, 'd':4, 'e':5}

chave = (input('Insira a chave desejada: '))
procuraValor(dic, chave)