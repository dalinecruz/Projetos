# -*- coding: iso-8859-1 -*-
'''
Created on 25 de abr. de 2022
Lista1 - Exercício4
@author: daline
'''
def tabelaPreco(taxaAumento):
    valorIngresso = 5.00
    numeroPessoas = 120
    custo = 200
    valorReducao = 0.50
    lucro = (valorIngresso * numeroPessoas) - custo
    melhorPreco = 0.0
    melhorLucro = 0
    print("Valor do Ingresso " +"Numero de Pessoas " + "Lucro ")

    while(valorIngresso >= 1):
        if(melhorLucro < lucro):
            melhorPreco = valorIngresso
            melhorLucro = lucro
            print(str(valorIngresso) + "" + str(numeroPessoas) + " " + str(lucro))
            valorIngresso -= valorReducao
            numeroPessoas += taxaAumento
            lucro = (valorIngresso * numeroPessoas) - custo
            print("\nO MelhorPreço do Ingresso será : R$ " + str(melhorPreco) + " com um lucro de R$ " + str(melhorLucro))

def calculaSessao():
    mediaPublico = 120
    mediaIngresso = 5.0
    custo = 200
    lucro = 0.0
    
    opcao = 0
    
    while(True):
        opcao = int(input("Sessões \n" + "1) Incluir Sessão " + "\n" + "2) Bilheteria" +  "\n" + "3) Reduzir Ingresso" +  "\n" + "4) Finalizar" +  "\n"))
     
     
        if(opcao > 4 or opcao < 1):
            print("Opção Invalida")
            continue
         
        if(opcao == 4):
            break
         
        if(opcao == 1):
            lucro += (mediaPublico * mediaIngresso) - custo
        
        if(opcao == 2):
            print("Publico = " + str(mediaPublico))
            print("Lucro = " + str(lucro))
            print("Valor Ingresso = " + str(mediaIngresso))
             
        if(opcao == 3):
            if(mediaIngresso == 1):
                print("Valor do ingresso não pode ser reduzido")
                  
            mediaPublico += 30
            mediaIngresso -= 0.50
            print("Valor Ingresso = " + str(mediaIngresso))
            print("Publico = " + str(mediaPublico))
        
        print(" ")   

taxaAumento = int(input("Informe a taxa de aumento do publico: "))
tabelaPreco(taxaAumento)

