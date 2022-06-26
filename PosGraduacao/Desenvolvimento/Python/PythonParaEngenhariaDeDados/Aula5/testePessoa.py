# -*- coding: iso-8859-1 -*-
from Aula5.PessoaFisica import Pessoa_Fisica
from Aula5.PessoaJuridica import Pessoa_Juridica

pf = Pessoa_Fisica()

pf.cpf =  int(input("\nInforme seu CPF :"))
pf.data_expedicao =  input("Informe a data de Expedição do CPF :")
pf.nome =  input("Informe seu Nome :")
pf.data_nascto =  input("Informe sua data de Nascimento :")
pf.idade = int(input("Informe sua Idade :"))

pf.imprimir()

pj = Pessoa_Juridica()

pj.nome =  input("\nInforme seu Nome :")
pj.cnpj =  input("Informe seu CNPJ :")
pj.endereco = input("Informe seu endereço :")
pj.data_criacao = int(input("Informe a data de criação :"))
pj.idade = int(input("Informe sua Idade :"))

pj.imprimir()