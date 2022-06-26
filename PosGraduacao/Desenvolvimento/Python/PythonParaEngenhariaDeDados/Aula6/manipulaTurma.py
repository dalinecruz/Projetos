'''
Created on 10 de mai. de 2022

@author: daline
'''
from Aula6.Aluno import Aluno

def lerTurma(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    tamanho = arquivo.readlines()
    cont = 0
    listaAlunos = []
    aluno = Aluno()
    while(len(tamanho) > cont):
        linha = tamanho[cont]
        vetor = linha.split(";")
        aluno = Aluno()
        aluno.nome = vetor[0]
        aluno.matricula = int(vetor[1])
        aluno.nota1 = float(vetor[2])
        aluno.nota2 = float(vetor[3])
        aluno.media = (aluno.nota1 + aluno.nota2) / 2.0
        listaAlunos.append(aluno)
        cont += 1
    arquivo.close()
    return listaAlunos

def gravaTurma(nomeArquivo, listaAluno, situacao):
    arquivo = open(nomeArquivo, "w+")
    
    for aluno in listaAluno:
        if(situacao == "M"):
            arquivo.write(aluno.nome + ";" + str(aluno.matricula) + ";" + str(aluno.media) + "\n")
        elif(situacao == "A"):
            if(aluno.media >= 6):
                arquivo.write(aluno.nome + ";" + str(aluno.matricula) + ";" + str(aluno.media) + "\n")
        else:
            if(aluno.media < 6):
                arquivo.write(aluno.nome + ";" + str(aluno.matricula) + ";" + str(aluno.media) + "\n")

    arquivo.close()    
        
listaAlunos = lerTurma("turma.txt") 
gravaTurma("MediaAlunos.txt", listaAlunos, "M")
gravaTurma("AlunosReprovados.txt", listaAlunos, "R")
gravaTurma("AlunosAprovados.txt", listaAlunos, "A")
