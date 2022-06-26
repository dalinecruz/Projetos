# -*- coding: iso-8859-1 -*-
from Aula2.ClassAutomovel import Automovel

lista = []

for x in range(2):
    a = Automovel()
    a.ano_fabricacao = int(input("Informe o ano de fabricação: "))
    a.chassi = input("Informe o chassi: ")
    a.cor = input("Informe a cor: ")
    a.marca = input("Informe a marca: ")
    a.modelo = input("Informe o modelo: ")
    a.numero_portas = int(input("Informe o num de portas: "))
    a.placa = input("Informe a placa: ")
    a.potencia = input("Informe a potencia: ")
    a.tipo = input("Informe o tipo: \n")
    lista.append(a)
    
for a in lista:
    a.imprimir(a)
    a.ligar(a)
    a.desligar(a)
    a.frear(a)
    a.travarPortas(a)
    a.acelerar(a)
    
    