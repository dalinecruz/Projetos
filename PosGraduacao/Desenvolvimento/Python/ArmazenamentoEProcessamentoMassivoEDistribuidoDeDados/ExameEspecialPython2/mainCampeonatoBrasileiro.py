# -*- coding: iso-8859-1 -*-
'''
Created on 03 de set. de 2022

@author: daline
'''
import pandas as pd
from ExameEspecialPython2.CampeonatoBrasileiro import CampeonatoBrasileiro

def leArquivo(nomeArquivo):
    campeonato = []
    arquivo = open(nomeArquivo + ".txt", "r")
    tamanho = arquivo.readlines()
    cont = 0
    
    while(len(tamanho) > cont):
        jogo = CampeonatoBrasileiro()
        linha = tamanho[cont]
        dados = linha.split(";")
        jogo.rodada = dados[0]
        jogo.data = dados[1]
        jogo.horario = dados[2]
        jogo.dia_jogo = dados[3]
        jogo.time_mandante = dados[4]
        jogo.time_visitante = dados[5]
        jogo.time_vencedor = dados [6]
        jogo.campo = dados [7]
        jogo.placar_mandante = dados [8]
        jogo.placar_visitante = dados [9]
        jogo.estado_mandante = dados[10]
        jogo.estado_visitante = dados[11]
        jogo.estado_vencedor = dados[12]
        campeonato.append(jogo)
        cont += 1
    arquivo.close()
    return campeonato
        
def grava_mandantesCampeoes(nomeArquivo, campeonato):
    arquivo = open(nomeArquivo, "w+")
    lista_mandantesCampeoes = []
    campeao = ""
    
    for dados in campeonato:
        if(dados.time_mandante == dados.time_vencedor):
            campeao = dados
            lista_mandantesCampeoes.append(campeao)
            
    for time in lista_mandantesCampeoes:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante + ";" + time.time_visitante + ";" + time.time_vencedor.upper() + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()

def grava_visitantesCampeoes(nomeArquivo, campeonato):
    arquivo = open(nomeArquivo, "w+")
    lista_visitantesCampeoes = []
    campeao = ""
    
    for dados in campeonato:
        if(dados.time_visitante == dados.time_vencedor):
            campeao = dados
            lista_visitantesCampeoes.append(campeao)
            
    for time in lista_visitantesCampeoes:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante + ";" + time.time_visitante + ";" + time.time_vencedor.upper() + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()
    
def grava_jogosUp(nomeArquivo, campeonato):
    arquivo = open(nomeArquivo, "w+")
    lista_jogos = []
    jogo = ""
    
    for dados in campeonato:
        jogo = dados
        lista_jogos.append(jogo)
            
    for time in lista_jogos:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante.upper() + ";" + time.time_visitante.upper() + ";" + time.time_vencedor.upper() + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()
    
def grava_jogosTimePerdeu(nomeArquivo, campeonato, time):
    arquivo = open(nomeArquivo, "w+")
    lista_jogos = []
    time = str(time)
    jogo = ""
    
    for dados in campeonato:
        if(time in dados.time_mandante):
            if(dados.time_vencedor != '-' and time not in dados.time_vencedor):
                jogo = dados
                lista_jogos.append(jogo)
        if(time in dados.time_visitante):
            if(dados.time_vencedor != '-' and time not in dados.time_vencedor):
                jogo = dados
                lista_jogos.append(jogo)
            
    for time in lista_jogos:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante.upper() + ";" + time.time_visitante.upper() + ";" + time.time_vencedor.upper() + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()
      
def gravaTime_mandanteCampeao(nomeArquivo, campeonato, time):
    arquivo = open(nomeArquivo, "+w")
    lista_timeCampeao = []
    time = str(time)
    campeao = ""
    
    for dados in campeonato:
        if(time == dados.time_vencedor):
            campeao = dados
            lista_timeCampeao.append(campeao)
            
    for time in lista_timeCampeao:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante + ";" + time.time_visitante + ";" + time.time_vencedor + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()
    
def gravaTime_visitanteCampeao(nomeArquivo, campeonato, time):
    arquivo = open(nomeArquivo, "+w")
    lista_timeCampeao = []
    time = str(time)
    campeao = ""
    
    for dados in campeonato:
        if(time == dados.time_vencedor):
            campeao = dados
            lista_timeCampeao.append(campeao)
            
    for time in lista_timeCampeao:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante + ";" + time.time_visitante + ";" + time.time_vencedor + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()
         
#Le arquivo original com todos os jogos                  
lista_jogos = leArquivo("jogos")
#Separa em dois arquivos de capeoes: mandantes e visitantes
grava_mandantesCampeoes("mandantesCampeoes.txt", lista_jogos)
grava_visitantesCampeoes("visitantesCampeoes.txt", lista_jogos)
grava_jogosUp("jogosUp.txt", lista_jogos)
jogos_up = leArquivo("jogosUp")
#Recebe o time favorito para filtragem
time = input("Informe o seu time: ")
#Grava jogos que o time não venceu
grava_jogosTimePerdeu("jogos"+time+"Perdeu.txt", jogos_up, time.upper())
#Le arquivo de mandantes vencedores e perdedores
timeCampeao = leArquivo("mandantesCampeoes")
#Grava arquvivo com os jogos em que o time venceu como mandante
gravaTime_mandanteCampeao(time+"_mandanteCampeao.txt", timeCampeao, time.upper())
#Le arquivo de visitantes vencedores e perdedores
timeCampeao = leArquivo("visitantesCampeoes")
#Grava arquvivo com os jogos em que o time venceu como visitante
gravaTime_visitanteCampeao(time+"_visitanteCampeao.txt", timeCampeao, time.upper())
#Cria Dataframes iniciais
df_visitante = pd.read_csv(time+"_visitanteCampeao.txt", delimiter= ';', names=['Rodada','Data', 'Horário', 'Dia do Jogo', 'Mandante', 'Visitante', 'Vencedor', 'Campo', 'Placar Mandante', 'Placar Visitante', 'Estado Mandante', 'Estado Visitante', 'Estado Vencedor'])
df_mandante = pd.read_csv(time+"_mandanteCampeao.txt", delimiter= ';', names=['Rodada','Data', 'Horário', 'Dia do Jogo', 'Mandante', 'Visitante', 'Vencedor', 'Campo', 'Placar Mandante', 'Placar Visitante', 'Estado Mandante', 'Estado Visitante', 'Estado Vencedor'])
#Especifica o nome da planilha a ser gerada
file_name = time+"_vitorias.xlsx"
#file_name2 = time+"_mandanteCampeao.xlsx"
#Exclui as colunas desnecessarias
df_visitante2 = df_visitante.loc[:, ~df_visitante.columns.isin(['Rodada', 'Data', 'Horário', 'Dia do Jogo', 'Vencedor', 'Campo', 'Estado Mandante', 'Estado Visitante', 'Estado Vencedor'])]
df_mandante2 = df_mandante.loc[:, ~df_mandante.columns.isin(['Rodada', 'Data', 'Horário', 'Dia do Jogo', 'Vencedor', 'Campo', 'Estado Mandante', 'Estado Visitante', 'Estado Vencedor'])]
#Renomeia as colunas
df_visitante3 = df_visitante2.set_axis(['Adversário', 'Meu time', 'Placar do adversário', 'Placar do '+time.capitalize()], axis=1, inplace=False)
df_mandante3 = df_mandante2.set_axis(['Meu time', 'Adversário', 'Placar do '+time.capitalize(), 'Placar do adversário'], axis=1, inplace=False)
#Duplica coluna para criar coluna de mando de campo
df_visitante3['Mando de campo'] = df_visitante3['Adversário'] 
df_mandante3['Mando de campo'] = df_mandante3['Meu time'] 
#Reordena as colunas
df_visitante3.reindex(columns=['Meu time', 'Adversário', 'Mando de campo', 'Placar do '+time.capitalize(), 'Placar do adversário'])
df_mandante3.reindex(columns=['Meu time', 'Adversário', 'Mando de campo', 'Placar do '+time.capitalize(), 'Placar do adversário'])
#Masclando os dataframes criados
df_mesclado_vitorias = pd.concat([df_visitante3, df_mandante3])
#Gerando a planilha de vitorias
df_mesclado_vitorias.reset_index(drop=True).to_excel(file_name)
#Exibe mensagem
print("Planilha gerada com sucesso!")
            