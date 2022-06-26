# -*- coding: iso-8859-1 -*-
'''
Created on 7 de jun. de 2022

@author: daline
'''
from faker import Faker
from Aula9.Tarefa2Aluno import Aluno
from random import randrange
import pandas as pd

def popular_aluno(numero_alunos):
    lista_alunos = []
    fake = Faker('pt_BR')

    for x in range(numero_alunos):
        aluno = Aluno()
        aluno.nome = fake.name()
        aluno.faltas = randrange(1, 30, 1)
        aluno.descricao_prova = fake.text()
        aluno.notas = randrange(40, 100, 5)
        lista_alunos.append(aluno)
     
    return lista_alunos   


lista = popular_aluno(10)
df = pd.DataFrame([x.as_dict() for x in lista])
file_name = 'Exercicio.xlsx'
df.to_excel(file_name)
print("ok")