# -*- coding: iso-8859-1 -*-
class Pessoa():
    nome = None
    idade = None
    data_nascto = None
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.data_nascto = ""
    
    def busca_idade(self):
        return self.idade