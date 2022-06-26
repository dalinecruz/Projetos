# -*- coding: iso-8859-1 -*-
'''
Created on 25 de abr. de 2022
Lista1 - Exercício6
@author: daline
'''
print('Verifique se o número é primo!')

i = 2
n = int(input('\nInsira um número: '))

while n <= 0:
    print('\nVocê não inseriu um número válido, tente novamente!')
    n = int(input('\nInsira um número: '))
    
if n == 1:
    print('1 não é um número primo!')
else:
    if n == 2:
        print('2 é um número primo!')
    else:
        while i < n and n > 0:
            if n % i == 0:
                #print(i)
                print('{} não é um número primo!'.format(n))
                break
            else:
                #print(i)
                i += 1         
        else:
            if n <= 0:
                print('Você não inseriu um número válido! Execute o programa novamente!')
            else:
                print('{} é um número primo!'.format(n))