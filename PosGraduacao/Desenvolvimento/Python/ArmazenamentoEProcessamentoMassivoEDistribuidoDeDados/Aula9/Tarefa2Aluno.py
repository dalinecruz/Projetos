# -*- coding: iso-8859-1 -*-
'''
Created on 7 de jun. de 2022

@author: daline
'''
class Aluno():

    def __init__(self):
        self.nome = ""
        self.faltas = 0
        self.notas = 0.0
        self.descProva = ""
        
    def as_dict(self):
        return {
            "Nome": self.nome,
            "Faltas": self.faltas,
            "Nota": self.notas,
            "Prova": self.descProva}
