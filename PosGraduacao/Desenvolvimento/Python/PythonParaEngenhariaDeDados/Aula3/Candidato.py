# -*- coding: iso-8859-1 -*-
'''
Created on 26 de abr. de 2022
@author: daline
'''
class Candidato():
    nome = None
    legenda = None
    numero = None
    votos = None

def __init__(self):
    self.nome = ""
    self.legenda = ""
    self.numero = ""
    self.votos = 0
  
def contVotos(self, numero):
    if numero == self.numero:
        self.votos += 1
            
def vencedor(self):
    max(self.votos)
    return self.nome
        
def maisVotados(self, lista):
    lista.sort(reverse=True, key=self.votos)
    return lista        
    
def apuraVotos(self, lista):
    i = 0
    contV = 0
    contB = 0
    contN = 0
    while i < len(lista):
        if (self.nome[i] != 'Branco' or self.nome[i] != 'Nulo'):
            contV += self.votos[i]
        else:
            if self.nome == 'Branco':
                contB += self.votos[i]
            else:
                contN += self.votos[i]
        i += 1
        
    print('Esta eleição teve o total de {} votos'.format(contV+contB+contN))   
    print('O total de votos válidos é: {}'.format(contV))
    print('O total de votos brancos é: {}'.format(contB))
    print('O total de votos nulos é: {}'.format(contN))

    
    
            
        
        
    
    