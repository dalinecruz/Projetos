# -*- coding: iso-8859-1 -*-
'''
Created on 2 de mai. de 2022

@author: daline
'''

from ListaExercicios2 import Televisao

class Controle:

    def __init__(self):
        '''
        Constructor
        '''
        self.televisao = Televisao.Televisao()
        self.televisao.canal = 0
        self.televisao.volume = 0
        
    def trocarVolume(self, volume):
        if volume == '+':
            self.televisao.volume += 1
            print('\nVolume atual é: {}'.format(self.televisao.volume))
        else:
            if volume == '-':
                self.televisao.volume -= 1
                print('\nVolume atual é: {}'.format(self.televisao.volume))
            else:
                print('\nNão é possível alterar o volume com o valor informado!')

    def trocarCanal(self, canal):
        if canal == '+':
            self.televisao.canal += 1
            print('\nVocê está no canal: {}'.format(self.televisao.canal))
        else:
            if canal == '-':
                self.televisao.canal -= 1
                print('\nVocê está no canal: {}'.format(self.televisao.canal))
            else:
                self.televisao.canal = int(canal)
                print('\nVocê está no canal: {}'.format(self.televisao.canal))
    