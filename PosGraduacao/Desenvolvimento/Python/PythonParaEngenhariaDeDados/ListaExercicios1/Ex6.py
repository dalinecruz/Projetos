# -*- coding: iso-8859-1 -*-
'''
Created on 25 de abr. de 2022
Lista1 - Exerc�cio6
@author: daline
'''
print('Verifique se o n�mero � primo!')

i = 2
n = int(input('\nInsira um n�mero: '))

while n <= 0:
    print('\nVoc� n�o inseriu um n�mero v�lido, tente novamente!')
    n = int(input('\nInsira um n�mero: '))
    
if n == 1:
    print('1 n�o � um n�mero primo!')
else:
    if n == 2:
        print('2 � um n�mero primo!')
    else:
        while i < n and n > 0:
            if n % i == 0:
                #print(i)
                print('{} n�o � um n�mero primo!'.format(n))
                break
            else:
                #print(i)
                i += 1         
        else:
            if n <= 0:
                print('Voc� n�o inseriu um n�mero v�lido! Execute o programa novamente!')
            else:
                print('{} � um n�mero primo!'.format(n))