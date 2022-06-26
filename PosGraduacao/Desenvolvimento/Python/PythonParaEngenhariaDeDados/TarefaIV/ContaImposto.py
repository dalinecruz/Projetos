'''
Created on 15 de mai. de 2022

@author: daline
'''

from TarefaIV.Conta import Conta

class ContaImposto(Conta):
    
    def __init__(self):
        super().__init__()
        self.percent_Imposto = 0.0
        
    def calcularImposto(self, taxa):
        self.percent_Imposto = taxa
        saldo = super().consultar_saldo()
        imposto = saldo * taxa / 100
        novoSaldo = saldo - imposto
        super().saldo = novoSaldo
        return imposto
    
    def consultar_saldo(self):        
        return super().consultar_saldo()  
    
    def depositar(self, valor):
        super().depositar(valor)
        
    def sacar(self, valor):
        super().sacar(valor)