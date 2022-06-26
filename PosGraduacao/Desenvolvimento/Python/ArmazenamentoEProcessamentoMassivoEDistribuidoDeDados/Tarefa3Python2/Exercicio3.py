'''
Created on 14 de jun. de 2022

@author: daline
'''
import pandas as pd

def converte_csv_json(nomeArquivo):
    df = pd.read_csv (r'city.csv')
    df.to_json (r'city.json')
    
def converte_json_csv(nomeArquivo):
    df = pd.read_json (r'city.json')
    df.to_csv (r'city2.csv')
     
nomeArquivo = "city.csv"
##dados = le_arquivo(nomeArquivo)
converte_csv_json("")

converte_json_csv("")