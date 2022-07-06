'''
Created on 5 de jul. de 2022

@author: daline
'''
import boto3
import pandas as pd
import ssl
from io import StringIO
import matplotlib.pyplot as plt
from DataLake.MunicipioInfantil import MunicipioInfantil

def converteCSV (data):
    data.to_csv (r'arquivo.csv', index = None)

def mapEsperanca(nome_arquivo, qtde_esperanca):
    arquivo = open(nome_arquivo + ".csv", "r", encoding = "utf8")
    municipios = []
    tamanho = arquivo.readlines()
    cont = 0
    while(len(tamanho) > cont):
        municipio = MunicipioInfantil()
        linha = tamanho[cont]
        dados = linha.split(";")   
        municipio.nome_municipio = dados[2]
        municipio.esperanca = float(dados[3])
        municipios.append(municipio)
        cont += 1

    
    municipios.sort(key=lambda municipio: municipio.esperanca, reverse = True)   
    mapa = {}
    cont = 0
    for m in municipios:
        if(cont >= qtde_esperanca):
            break
        
        cont += 1
        mapa[m.nome_municipio] = m.esperanca
        
    
    return mapa

def mapMortalidade(nome_arquivo, qtde_mortalidade):
    arquivo = open(nome_arquivo + ".csv", "r", encoding = "utf8")
    municipios = []
    tamanho = arquivo.readlines()
    cont = 0
    while(len(tamanho) > cont):
        municipio = MunicipioInfantil()
        linha = tamanho[cont]
        dados = linha.split(";")   
        municipio.nome_municipio = dados[2]
        municipio.mortalidade = float(dados[4])
        municipios.append(municipio)
        cont += 1

    
    municipios.sort(key=lambda municipio: municipio.mortalidade, reverse = True)   
    mapa = {}
    cont = 0
    for m in municipios:
        if(cont >= qtde_mortalidade):
            break
        
        cont += 1
        mapa[m.nome_municipio] = m.mortalidade
        
    
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

 
def leArquivo():
    s3 = boto3.resource('s3', aws_access_key_id='AKIAUSA6HND622LYXMPD', aws_secret_access_key='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')
    bucket = s3.Bucket('datalake-pucminas')
    cont = 0  
   
    for obj in bucket.objects.filter(Prefix='planilhas/IDH2010.csv'):
        for line in obj.get()['Body'].read().decode('utf-8').splitlines():
            if(cont == 0):
                cont += 1
                continue
            
            dados = line.split(";")
            return dados

ssl._create_default_https_context = ssl._create_unverified_context    

data = leArquivo()

str_to_csv = StringIO(data)
df = pd.read_csv(str_to_csv, sep=";")

print(df)
converteCSV(df)

nome_arquivo = "arquivo"
mapa_reduce_esperanca  = mapEsperanca(nome_arquivo, 5)
mapa_reduce_mortalidade  = mapMortalidade(nome_arquivo, 5)

print(mapa_reduce_esperanca)
print(mapa_reduce_mortalidade)

'''grava_imagem(mapa_reduce_esperanca, "Maior_Esperanca.png")
grava_imagem(mapa_reduce_mortalidade, "Maior_Mortalidade.png")
'''