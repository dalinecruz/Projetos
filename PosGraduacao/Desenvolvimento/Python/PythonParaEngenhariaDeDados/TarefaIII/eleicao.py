# -*- coding: iso-8859-1 -*-
'''
Created on 5 de mai. de 2022

@author: daline
'''
from ListaExercicios2.Candidato import Candidato

lista = []
opcao = 0

while True:
    opcao = int(input("\nEleições Governador 2022 \n" 
                      + "\n1) Incluir Candidato " + "\n" 
                      + "2) Votar" + "\n" 
                      + "3) Apurar eleição" + "\n" 
                      + "4) Listar candidatos mais votados" +"\n" 
                      + "5) Sair\n" ))
    
    
    if opcao > 5 or opcao < 1:
        print("Opcao inválida, tente novamente! ")
        continue
    
    if(opcao == 5):
        print("Programa encerrado!")
        break
    
    if (opcao == 1):
        candidato = Candidato()
        candidato.nome = input('Nome: ')
        candidato.legenda = input('Legenda: ')
        candidato.numero = input('Numero: ')
        lista.append(candidato)

    if(opcao == 2):
        for dado in lista:
            print('Candidato: {} - Partido: {} -  Número: {} - Votos: {}'.format(dado.nome, dado.legenda, dado.numero, candidato.votos))
        i = 0
        numero = int(input('\nPara validar seu voto, informe o número do candidato: '))
        while i < len(lista):
            
        candidato.contVoto()
        lista[numero] = candidato
            
    if(opcao == 4):
        candidato.maisVotados(lista)
