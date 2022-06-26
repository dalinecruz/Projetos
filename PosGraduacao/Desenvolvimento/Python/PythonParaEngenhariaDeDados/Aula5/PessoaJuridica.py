# -*- coding: iso-8859-1 -*-
from Aula5.Pessoa import Pessoa

class Pessoa_Juridica(Pessoa):
    cnpj = None
    endereco = None
    data_criacao = None
    
    def __init__(self):
        self.cnpj = 0
        self.endereco = ""
        self.data_criacao = ""
        
    def imprimir(self):
        print("\nCNPJ ..........:" + str(self.cnpj))
        print("Endereco ......: " + str(self.endereco))
        print("Data Criacao ..:  " + str(self.data_criacao))
        print("Nome ......: " + self.nome)
        print("Idade ......: ".format(str(self.busca_idade())))
        print("Data Nascimento ..:  ".format(str(self.data_nascto)))