# -*- coding: iso-8859-1 -*-
'''
Created on 2 de mai. de 2022

@author: daline
'''

class Televisao:

    def __init__(self):
        '''
        Constructor
        '''
        self.canal = 0
        self.volume = 0
        
    def imprimir(self):
        print('\nO canal atual é {} e o volume é {}'.format(self.canal, self.volume))