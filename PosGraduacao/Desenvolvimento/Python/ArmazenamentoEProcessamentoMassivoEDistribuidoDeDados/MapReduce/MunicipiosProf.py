'''
Created on 5 de jul. de 2022

@author: daline
'''
from MapReduce.Municipio import Municipio
import matplotlib.pyplot as plt

def map(nome_arquivo, qtde_expectativa, flag_ordenacao):
    arquivo = open(nome_arquivo + ".txt", "r", encoding = "utf8")
    municipios = []
    tamanho = arquivo.readlines()
    cont = 0
    while(len(tamanho) > cont):
        municipio = Municipio()
        linha = tamanho[cont]
        dados = linha.split(";")   
        municipio.nome_municipio = dados[0]
        municipio.expectativa = float(dados[1])
        municipios.append(municipio)
        cont += 1

    
    municipios.sort(key=lambda municipio: municipio.expectativa, reverse = flag_ordenacao)   
    mapa = {}
    cont = 0
    for m in municipios:
        if(cont >= qtde_expectativa):
            break
        
        cont += 1
        mapa[m.nome_municipio] = m.expectativa
        
    
    return mapa


def grava_imagem(mapa, nome_arquivo):

    mapaPlot = {}
    cont = 0
    for i in sorted(mapa, key=mapa.get, reverse=True):
        if(cont > 10):
            break;
        
        cont += 1
        mapaPlot[i] = mapa[i]
        
    plt.barh(list(mapaPlot.keys()), mapaPlot.values())
    plt.gca().invert_yaxis()
    plt.savefig(nome_arquivo, format='png')
    plt.show()
    plt.close()

nome_arquivo = "MunicipiosExpectativa"
mapa_reduce_maior  = map(nome_arquivo, 10, True)
mapa_reduce_menor  = map(nome_arquivo, 10, False)

grava_imagem(mapa_reduce_maior, "Maior_Expectativa.png")
grava_imagem(mapa_reduce_menor, "Menor_Expectativa.png")