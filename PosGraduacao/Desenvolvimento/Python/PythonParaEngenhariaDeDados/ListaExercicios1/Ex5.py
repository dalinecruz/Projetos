# -*- coding: iso-8859-1 -*-
'''
Created on 25 de abr. de 2022
Lista1 - Exerc�cio5
@author: daline
'''
print('Este programa aceita apenas n�meros inteiros e positivos. Para encerrar, insira outro tipo de dado.')

lista = []

def somaPar(lista):
    soma = 0
    for num in lista:
        n = int(num)
        if n % 2 == 0:
            soma += n
    return soma

def somaImpar(lista):
    soma = 0
    for num in lista:
        if num % 2 != 0:
            soma += num
    return soma

while True:
    num = input('\nInsira um n�mero: ')
    if num.isnumeric() == True:
        intNum = int(num)
        if intNum > 0:
            lista.append(intNum)
        else:
            print('\nVoc� n�o informou um n�mero inteiro positivo e, por isso, o programa est� sendo encerrado!')
            print('\nOs n�meros digitados foram: ', lista)
            print('O resultado da soma dos n�meros pares � igual a ', somaPar(lista))
            print('O resultado da soma dos n�meros �mpares � igual a ', somaImpar(lista))
            break
    else:
        print('\nVoc� n�o informou um n�mero inteiro positivo e, por isso, o programa est� sendo encerrado!')
        print('\nOs n�meros digitados foram: ', lista)
        print('O resultado da soma dos n�meros pares � igual a ', somaPar(lista))
        print('O resultado da soma dos n�meros �mpares � igual a ', somaImpar(lista))
        break
    
        

            
    
    
