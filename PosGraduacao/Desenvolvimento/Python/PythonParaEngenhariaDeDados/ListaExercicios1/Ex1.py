# -*- coding: iso-8859-1 -*-
'''
Created on 24 de abr. de 2022
Lista1 - Exerc�cio1
@author: daline
'''
grade = {}
total = 0

while True:

    funcao = input('\nInforme a fun��o: ')
    salario = float(input ('informe o salario: '))
    grade.update({funcao:salario})
    opcao = input('Deseja continuar?(s/n): ')
    if opcao == 'n':
        for i in grade.values():
            total += i
        print (grade)
        print('A m�dia de sal�rios �: {:.2f} Reais.'.format(total / len(grade)))
        break
