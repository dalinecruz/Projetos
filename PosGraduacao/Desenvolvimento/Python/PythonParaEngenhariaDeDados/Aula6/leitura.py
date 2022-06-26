'''
Created on 10 de mai. de 2022

@author: daline
'''
from Aula6.Aluno import Aluno

arquivo = open("notas.txt", "r")

tamanho = arquivo.readlines()
cont = 0
listaAlunos = []

while(len(tamanho) > cont):
    linha = tamanho[cont]
    vetor = linha.split(";")
    aluno = Aluno()
    aluno.nome = vetor[0]
    aluno.matricula = int(vetor[1])
    aluno.nota1 = float(vetor[2])
    aluno.nota2 = float(vetor[3])
    listaAlunos.append(aluno)
    cont += 1

for dados in listaAlunos:
    print("Nome Aluno ..........: " + dados.nome)
    print("Matricula do Aluno ..: " + str(dados.matricula))
    print("Nota 1 ..............: " + str(dados.nota1))
    print("Nota 2 ..............: " + str(dados.nota2))
    print(" ")
    
arquivo.close()