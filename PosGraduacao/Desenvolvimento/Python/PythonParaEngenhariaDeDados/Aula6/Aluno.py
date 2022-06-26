'''
Created on 10 de mai. de 2022

@author: daline
'''
class Aluno:
    nome = None
    matricula = None
    nota1 = None
    nota2 = None
    media = None
    
    
    def __init__(self):
        self.nome = ""
        self.matricula = 0
        self.nota1 = 0.0
        self.nota2 = 0.0
        self.media = 0.0
        
    def calculaMedia(self, listaAlunos):
        maiorMedia = 0
        for dados in listaAlunos:
            if(dados.media > maiorMedia):
                maiorMedia = dados.media
                
        return maiorMedia        
                
    def imprimir(self, listaAlunos):
        for dados in listaAlunos:
            print("Nome Aluno ..........: " + dados.nome)
            print("Matricula do Aluno ..: " + str(dados.matricula))
            print("Nota 1 ..............: " + str(dados.nota1))
            print("Nota 2 ..............: " + str(dados.nota2))
            print("Media do Aluno ......: " + str(dados.media))
            print(" ")