# -*- coding: iso-8859-1 -*-
from Aula5.Pessoa import Pessoa

class Pessoa_Fisica(Pessoa):
    cpf = None
    data_expedicao = None
    
    def __init__(self):
        self.cpf = 0
        self.data_expedicao = ""
        
    def imprimir(self):
        print("\nCPF ..........:" + str(self.cpf))
        print("Data Expedição ..:  " + self.data_expedicao)
        print("Nome ......: " + self.nome)
        print("Idade ......: " + str(self.busca_idade()))
        print("Data Nascimento ..:  " + self.data_nascto)