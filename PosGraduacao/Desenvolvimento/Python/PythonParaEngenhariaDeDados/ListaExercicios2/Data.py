# -*- coding: iso-8859-1 -*-
'''
Created on 3 de mai. de 2022

@author: daline
'''

class Data():
    def __init__(self, dia, mes, ano):
        '''
        Constructor
        '''
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
        if self.valida():
            self.iprimirData()
        else:
            print("\nValores inválidos para uma data!")
            
     
    def valida(self): 
        lista_mes = [2,4,6,9,11]
        
        if not 1 <= self.dia <= 31:
            return False
        if self.dia == 31:
            for self.mes in lista_mes:
                return False
        if self.mes == 2 and self.dia == 30:
                return False
        if self.mes == 2 and self.dia == 29:
            if not self.ano % 4 == 0:
                return False
        if not 1 <= self.mes <= 12:
            return False 
        if self.ano < 1: 
            return False

        
    def iprimirData(self):
        print('\nA data informada é {:02}/{:02}/{}.'.format(self.dia,self.mes,self.ano))