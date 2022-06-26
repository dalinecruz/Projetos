# -*- coding: iso-8859-1 -*-
'''
Created on 15 de mai. de 2022

@author: daline
'''
  
class Conta:
    
    def __init__(self):
        self.numero: 0
        self.saldo: 0.0
    
    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
    
    
    
    