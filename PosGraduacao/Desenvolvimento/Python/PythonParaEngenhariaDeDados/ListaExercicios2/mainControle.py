# -*- coding: iso-8859-1 -*-
'''
Created on 3 de mai. de 2022

@author: daline
'''
from ListaExercicios2 import ControleRemoto

controle = ControleRemoto.Controle()
opcao = 0

while True:
    opcao = int(input("\nControle Remoto \n" 
                      + "\n1) Trocar canal " + "\n" 
                      + "2) Alterar volume" + "\n" 
                      + "3) Sair\n" ))

    if opcao > 3 or opcao < 1:
        print("Opcao Invalida ! ")
        continue
    
    if(opcao == 3):
        print('Controle remoto encerrado!')
        break
   
    if(opcao == 1):
        controle.televisao.imprimir()
        canal = input('\nInsira \'+\' para subir o canal,\'-\' para descer o canal, ou insira o canal desejado: ')
        controle.trocarCanal(canal)

    if(opcao == 2):
        controle.televisao.imprimir()
        volume = input('\nInsira \'+\' para aumentar o volume ou \'-\' para diminuir: ')
        controle.trocarVolume(volume)
