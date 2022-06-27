# -*- coding: iso-8859-1 -*-
'''
Created on 21 de jun. de 2022

@author: daline
'''
import matplotlib.pyplot as plt

def map (nome_arquivo):
    arquivo = open(nome_arquivo + ".txt", "r", encoding = "utf8")
    municipios = {}
    tamanho = arquivo.readlines()
    cont = 0
    while(len(tamanho) > cont):
        linha = tamanho[cont]
        dados = linha.split(";")   
        if(cont == 0):
            cont += 1
            continue;
        municipio = dados[0]
        expect = dados[1]
        cont += 1
        
        for i in range(len(municipio)-1):
            municipios[municipio[i]] = expect[i]
    
    #municipios.sort(key=None, reverse=True)
    '''mapa = {}
    
    for municipio in municipios:
        mapa[municipio] = municipios.)
    ''' 
    return municipios


def reduce_mapa(mapa):
    chave = ""
    valor = 0
    
    for nome in mapa:
        if(mapa[nome] > valor):
            chave = nome
            valor = mapa[nome]
    
    reduce = {}
    reduce[chave] = valor
    return reduce


def grava_imagem(mapa):

    mapaPlot = {}
    cont = 0
    for i in sorted(mapa, key=mapa.get, reverse=True):
        if(cont > 10):
            break;
        
        cont += 1
        mapaPlot[i] = mapa[i]
        
    plt.barh(list(mapaPlot.keys()), mapaPlot.values())
    plt.gca().invert_yaxis()
    plt.savefig('teste.png', format='png')
    plt.show()
    plt.close()


mapa = map("MunicipiosExpectativa")
print(mapa)
#mapa_reduce = reduce_mapa(mapa)    
#grava_imagem(mapa)