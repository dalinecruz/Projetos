# -*- coding: iso-8859-1 -*-
'''
Created on 21 de mai. de 2022

@author: daline
'''
from TarefaIV.Ingresso import Ingresso

class IngressoVIP(Ingresso):
    def __init__(self):
        self.valor_extra = 0.0
        
    def valorVIP(self):
        valorNormal = super().retornaValor()
        valorVip = valorNormal + self.valor_extra
        return valorVip