# -*- coding: iso-8859-1 -*-
'''
Created on 26 de abr. de 2022
Lista1 - Exercício10
@author: daline
'''

def inss (salarioB):
    if salarioB <= 1212:
        descontoInss = salarioB * 0.075
        return descontoInss
    else:
        if salarioB > 1212 and salarioB <= 2427.35:
            descontoInss = salarioB * 0.09
            return descontoInss
        else:
            if salarioB > 2427.35 and salarioB <= 3641.03:
                descontoInss = salarioB * 0.12
                return descontoInss
            else:
                if salarioB > 3641.03 and salarioB <= 7087.22:
                    descontoInss = salarioB * 0.14
                    return descontoInss
                else:
                    descontoInss = 466.18
                    return descontoInss

def irpf (salarioB):
    if salarioB <= 1903.98:
        descontoIrpf = 0
        return descontoIrpf
    else:
        if salarioB > 1903.98 and salarioB <= 2826.65:
            descontoIrpf = salarioB * 0.075
            return descontoIrpf
        else:
            if salarioB > 2826.65 and salarioB <= 3751.05:
                descontoIrpf = salarioB * 0.15
                return descontoIrpf
            else:
                if salarioB > 3751.05 and salarioB <= 4664.68:
                    descontoIrpf = salarioB * 0.225
                    return descontoIrpf
                else:
                    descontoIrpf = salarioB * 0.275
                    return descontoIrpf

print('Calcule seu salário líquido!')
salarioB = float(input('\nInforme o seu salário: '))

totalDesc = inss(salarioB) + irpf(salarioB)
salarioL = salarioB - totalDesc

print('\nO desconto de INSS é: R$ {:.2f}'.format(inss(salarioB)))
print('O desconto de IRPF é: R$ {:.2f}'.format(irpf(salarioB)))
print('O total de descontos é: R$ {:.2f}'.format(totalDesc))
print('\nSeu salário líquido é: R$ {:.2f}'.format(salarioL))
