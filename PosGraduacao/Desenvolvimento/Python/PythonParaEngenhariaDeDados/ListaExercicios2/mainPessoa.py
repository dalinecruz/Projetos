# -*- coding: iso-8859-1 -*-
from ListaExercicios2 import Pessoa

pessoa = Pessoa.Pessoa()

pessoa._nome = input("Digite seu nome: ")
pessoa._idade = input("Digite sua idade: ")
pessoa._altura = input("Digite sua altura em cm: ")

pessoa.imprimirDados()
