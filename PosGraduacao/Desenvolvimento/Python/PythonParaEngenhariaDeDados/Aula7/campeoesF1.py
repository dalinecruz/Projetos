'''
Created on 17 de mai. de 2022

@author: daline
'''
import matplotlib.pyplot as plt
from Aula7.PilotoF1 import PilotoF1

def leArquivo(nomeArquivo):
    campeoes = []
    arquivo = open(nomeArquivo + ".txt", "r")
    tamanho = arquivo.readlines()
    cont = 0
    while(len(tamanho) > cont):
        p = PilotoF1()
        linha = tamanho[cont]
        dados = linha.split(";")
        p.anoTitulo = int(dados[0])
        p.nacionalidade = dados[1]
        p.nomePiloto = dados[2].replace("1","").strip()
        p.equipe = dados[3].strip()
        cont += 1
        campeoes.append(p)
    arquivo.close()
    return campeoes

def nacionalidades(listaTitulos):
    dicionario = {}
    lista = []
    listaNacionalidade = []
    nacionalidade = ""
    for dados in listaTitulos:
        if(nacionalidade != dados.nacionalidade):
            nacionalidade = dados.nacionalidade
            lista.append(nacionalidade)
        else:
            nacionalidade = dados.nacionalidade
            
        listaNacionalidade.append(nacionalidade)
    
   
    for dados in lista:
        dicionario[dados] = listaNacionalidade.count(dados)
    
    resultado = {}
    cont = 0
    for i in sorted(dicionario, key = dicionario.get, reverse=True):
            if(cont >=5):
                break
        
            print(i , " ::" , dicionario[i])
            resultado[i] = dicionario[i]
            cont += 1
            
    plt.bar(resultado.keys(), resultado.values())
    plt.show()
    
def equipes(listaTitulos):
    dicionario = {}
    lista = []
    listaEquipe = []
    equipe = ""
    for dados in listaTitulos:
        if(equipe != dados.equipe):
            equipe = dados.equipe
            lista.append(equipe)
        else:
            equipe = dados.equipe
            
        listaEquipe.append(equipe)
    
   
    for dados in lista:
        dicionario[dados] = listaEquipe.count(dados)
    
    resultado = {}
    cont = 0
    for i in sorted(dicionario, key = dicionario.get, reverse=True):
            if(cont >=5):
                break
        
            print(i , " ::" , dicionario[i])
            resultado[i] = dicionario[i]
            cont += 1
            
    plt.bar(resultado.keys(), resultado.values())
    plt.show()
    
listaCampeoes = leArquivo("formula1")
nacionalidades(listaCampeoes)
equipes(listaCampeoes)