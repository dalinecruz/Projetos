# -*- coding: iso-8859-1 -*-
'''
Created on 5 de mai. de 2022

@author: daline
'''
class Candidato():
    
    def __init__(self):
        self.nome = ""
        self.legenda = ""
        self.numero = ""
        self.votos = 0

    def contVoto(self):
        self.votos += 1

    def maisVotados(self, lista):
        dicVotos = {cand.nome: cand.votos for cand in lista}
        print(dicVotos)
            
    # for key in sorted(dicVotos.keys(), reverse=True):
        #    print(key[0], ":", key[1] )

             
    def apuraVotos(self, lista):
        i = 0
        contV = 0
        contB = 0
        contN = 0
        for i in range(len(lista)):
            if (self.nome[i] != 'Branco' or self.nome[i] != 'Nulo'):
                voto = lista.votos[i]
                contV += voto
            else:
                if self.nome == 'Branco':
                    voto = lista.votos[i]
                    contB += voto
                else:
                    contN += voto
            i += 1
            
        print('Esta eleição teve o total de {} votos'.format(str(contV+contB+contN)))   
        print('O total de votos válidos é: {}'.format(str(contV)))
        print('O total de votos brancos é: {}'.format(str(contB)))
        print('O total de votos nulos é: {}'.format(str(contN)))   