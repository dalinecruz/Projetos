# -*- coding: iso-8859-1 -*-
'''
Created on 21 de mai. de 2022

@author: daline
'''
from TarefaIV.IngressoVIP import IngressoVIP

precoVIP = IngressoVIP()

precoVIP.valor = float(input("Informe o pre�o do Ingresso: R$"))
precoVIP.valor_extra = float(input("Informe o valor adicional para aplicar ao ingresso VIP: R$"))

print("O valor do ingresso �: R$", precoVIP.retornaValor())
print("O valor do ingresso VIP �: R$", precoVIP.valorVIP())