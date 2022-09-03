# -*- coding: iso-8859-1 -*-
'''
Created on 03 de set. de 2022

@author: daline
'''
import pandas as pd
from ExameEspecialPython2.CampeonatoBrasileiro import CampeonatoBrasileiro

def leArquivo(nomeArquivo):
    campeonato = []
    arquivo = open(nomeArquivo + ".txt", "r", encoding = "latin-1")
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
    
def gravaTimes_maiusculo(nomeArquivo, campeonato):
    arquivo = open(nomeArquivo, "+w")
    
    for dados in campeonato:
        arquivo.write(str(dados.rodada + ";" + dados.data + ";" + dados.horario + ";" + dados.dia_jogo + ";" + dados.time_mandante.upper() + ";" + dados.time_visitante.upper() + ";" + dados.time_vencedor.upper() + ";" + dados.campo + ";" + dados.placar_mandante + ";" + dados.placar_visitante + ";" + dados.estado_mandante + ";" + dados.estado_visitante + ";" + dados.estado_vencedor))
    arquivo.close()
    
def gravaDerrotas_time(nomeArquivo, campeonato, time):
    arquivo = open(nomeArquivo, "+w")
    lista_derrotasTime = []
    time = str(time)
    derrota = ""
    
    for dados in campeonato:
        if (time == dados.time_mandante and time != dados.time_vencedor):
            derrota = dados
            lista_derrotasTime.append(derrota)
            
    for time in lista_derrotasTime:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante + ";" + time.time_visitante + ";" + time.time_vencedor + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()

#Lê arquivo original com todos os jogos                  
lista_jogos = leArquivo("jogos")
#Separa em dois arquivos de capeoes: mandantes e visitantes
grava_mandantesCampeoes("mandantesCampeoes.txt", lista_jogos)
grava_visitantesCampeoes("visitantesCampeoes.txt", lista_jogos)
gravaTimes_maiusculo("times_up.txt", lista_jogos)

#Grava nova lista com os nomes dos times em maiúsculo
lista_jogosUp = leArquivo("times_up")

#Recebe o time para filtrar
time = input("Informe o seu time: ")

#Lê arquivo de mandantes vencedores
timeCampeao = leArquivo("mandantesCampeoes")

#Grava arquvivo com os jogos em que o time venceu como mandante
gravaTime_mandanteCampeao(time+"_mandanteCampeao.txt", timeCampeao, time.upper())

#Lê arquivo de visitantes vencedores
timeCampeao = leArquivo("visitantesCampeoes")

#Grava arquvivo com os jogos em que o time venceu como visitante
gravaTime_visitanteCampeao(time+"_visitanteCampeao.txt", timeCampeao, time.upper())

#Grava arquvivo com todas os jogos perdidos pelo time indicado
gravaDerrotas_time(time+"_Vencido.txt", lista_jogosUp, time.upper())

#gera xlsx
df = pd.read_csv(time+"_visitanteCampeao.txt", delimiter= ';', names=['Rodada','Data', 'Horário', 'Dia do Jogo', 'Mandante', 'Visitante', 'Vencedor', 'Campo', 'Placar Mandante', 'Placar Visitante', 'Estado Mandante', 'Estado Visitante', 'Estado Vencedor'])
file_name = time+"_visitanteCampeao.xlsx"
df.to_excel(file_name)
print("ok")
            