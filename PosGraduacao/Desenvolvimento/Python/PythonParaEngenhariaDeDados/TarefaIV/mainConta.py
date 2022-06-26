# -*- coding: iso-8859-1 -*-
'''
Created on 15 de mai. de 2022

@author: daline
'''
from TarefaIV.ContaImposto import ContaImposto

lista_conta = []
opcao = 0

while True:
    opcao = int(input("\nConta Imposto \n"
                      + "\n1) Cadastrar nova conta " + "\n"
                      + "2) Depositar " + "\n" 
                      + "3) Sacar" + "\n" 
                      + "4) Consultar saldo" + "\n" 
                      + "5) Calcular imposto" +"\n" 
                      + "6) Sair\n" ))
    
    
    if opcao > 6 or opcao < 1:
        print("Opcao inválida, tente novamente! ")
        continue
    
    if(opcao == 6):
        print("Programa encerrado!")
        break
    
    if (opcao == 1):
        conta_imposto = ContaImposto()
        conta_imposto.numero = input('Número da conta: ')
        conta_imposto.saldo = 0.0
        lista_conta.append(conta_imposto)
    
    if(opcao == 2):
        num = int(input('Informe o número da conta: '))
        for conta in lista_conta:
            n = int(conta.numero)
            if n == num:
                valor = float(input('Digite o valor que deseja depositar: R$'))
                conta_imposto = conta
                conta_imposto.depositar(valor)
                print('\nDepósito realizado!')
                break
               
                
    if(opcao == 3):      
        num = int(input('Informe o número da conta: '))
        for conta in lista_conta:
            n = int(conta.numero)
            print(n)
            if n == num:
                conta_imposto.sacar(float(input('Digite o valor que deseja sacar: R$')))
                print('\nSaque realizado!')        


    if(opcao == 4):
        num = int(input('Informe o número da conta: '))
        for conta in lista_conta:
            n = int(conta.numero)
            if n == num:
                print('\nO saldo na conta {} é: R${:.2f}'.format(conta.numero,conta_imposto.consultar_saldo()))

        
    if(opcao == 5):
        conta_imposto.calcularImposto(float(input('Digite a taxa a ser aplicada: ')))
        print('O imposto a ser cobrado é: {:.2f}'.format(conta_imposto.calcularImposto))

