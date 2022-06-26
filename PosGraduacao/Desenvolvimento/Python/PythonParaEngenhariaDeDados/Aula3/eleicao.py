# -*- coding: iso-8859-1 -*-
'''
Created on 26 de abr. de 2022
@author: daline
'''
from ListaExercicios2 import Candidato

lista = []
opcao = 0

while True:
    opcao = int(input("\nEleições Governador 2022 \n" 
                      + "\n1) Incluir Candidato " + "\n" 
                      + "2) Votar" + "\n" 
                      + "3) Apurar votação" +"\n" 
                      + "4) Sair\n" ))
    
    
    if opcao > 4 or opcao < 1:
        print("Opcao Invalida ! ")
        continue
    
    if(opcao == 4):
        break
    
    if (opcao == 1):
        candidato = Candidato
        candidato.nome = input('Nome: ')
        candidato.legenda = input('Legenda: ')
        candidato.numero = input('Numero: ')
        lista.append(candidato)

    if(opcao == 2):
        for dados in lista:
            print('Candidato: {} - Número: {}'.format(candidato.nome, candidato.numero))
        numero = input('\nPara validar seu voto, informe o número do candidato: ')
        candidato.contVotos(numero)

        
    if(opcao == 3):
        print('O vencedor e novo governador é : {}'.format(candidato.vencedor()))
        print("")
        candidato.apuraVotos(lista)
        print("")
        candidato.maisVotados()
