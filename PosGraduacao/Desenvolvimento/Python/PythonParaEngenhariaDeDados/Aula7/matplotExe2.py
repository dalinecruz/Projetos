'''
Created on 17 de mai. de 2022

@author: dalin
'''
import matplotlib.pyplot as plt

salarios = {"Medico": 30000,"Engenheiro": 20000, "Advogado": 15000}

salarioOrdenado = {}

print(sorted(salarios))

for i in sorted(salarios, key = salarios.get):

    print(i, salarios[i])

    salarioOrdenado[i] = salarios[i]


plt.plot(salarioOrdenado.keys(), salarioOrdenado.values())

plt.show()