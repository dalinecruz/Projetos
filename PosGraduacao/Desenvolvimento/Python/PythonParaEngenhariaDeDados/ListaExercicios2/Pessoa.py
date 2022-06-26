# -*- coding: iso-8859-1 -*-
'''
Created on 2 de mai. de 2022

@author: daline
'''
class Pessoa:

    def __init__(self):
        '''
        Constructor
        '''
        self._nome = ''
        self._idade = 0
        self._altura = 0
        
    def imprimirDados(self):
        print('{} tem {} anos e {} centímetros de altura'.format(self._nome, self._idade, self._altura))
        