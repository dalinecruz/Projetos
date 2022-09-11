# -*- coding: iso-8859-1 -*-
'''
Created on 03 de set. de 2022

@author: daline
'''
import matplotlib.pyplot as plt
import pandas as pd
import os
from ExameEspecialPython2.CampeonatoBrasileiro import CampeonatoBrasileiro

##Lê o arquvio de jogos##
def leArquivo(nomeArquivo):
    campeonato = []
    arquivo = open(nomeArquivo + ".txt", "r", encoding = 'UTF-8')
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

##Grava arquivo com todas as partidas cujos mandantes venceram##     
def grava_mandantesCampeoes(nomeArquivo, campeonato):
    arquivo = open(nomeArquivo, "w+", encoding = 'UTF-8')
    lista_mandantesCampeoes = []
    campeao = ""
    
    for dados in campeonato:
        if(dados.time_mandante == dados.time_vencedor):
            campeao = dados
            lista_mandantesCampeoes.append(campeao)
            
    for time in lista_mandantesCampeoes:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante + ";" + time.time_visitante + ";" + time.time_vencedor.upper() + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()

##Grava arquivo com todas as partidas cujos visitantes venceram##   
def grava_visitantesCampeoes(nomeArquivo, campeonato):
    arquivo = open(nomeArquivo, "w+", encoding = 'UTF-8')
    lista_visitantesCampeoes = []
    campeao = ""
    
    for dados in campeonato:
        if(dados.time_visitante == dados.time_vencedor):
            campeao = dados
            lista_visitantesCampeoes.append(campeao)
            
    for time in lista_visitantesCampeoes:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante + ";" + time.time_visitante + ";" + time.time_vencedor.upper() + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()
    
##Grava arquivo com todos os times em mandante, visitante e vencedor com letras maiúsculasm##    
def grava_jogosUp(nomeArquivo, campeonato):
    arquivo = open(nomeArquivo, "w+", encoding = 'UTF-8')
    lista_jogos = []
    jogo = ""
    
    for dados in campeonato:
        jogo = dados
        lista_jogos.append(jogo)
            
    for time in lista_jogos:
        arquivo.write(str(time.rodada + ";" + time.data + ";" + time.horario + ";" + time.dia_jogo + ";" + time.time_mandante.upper() + ";" + time.time_visitante.upper() + ";" + time.time_vencedor.upper() + ";" + time.campo + ";" + time.placar_mandante + ";" + time.placar_visitante + ";" + time.estado_mandante + ";" + time.estado_visitante + ";" + time.estado_vencedor))
    arquivo.close()
    
##Grava arquivo com todas as partidas perdidas pelo time informado##
def grava_jogosTimePerdeu(nomeArquivo, campeonato, time):
    arquivo = open(nomeArquivo, "w+", encoding = 'UTF-8')
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

##Grava arquivo com todas as partidas vencidas pelo time informado enquanto mandante##     
def gravaTime_mandanteCampeao(nomeArquivo, campeonato, time):
    arquivo = open(nomeArquivo, "+w", encoding = 'UTF-8')
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

##Grava arquivo com todas as partidas vencidas pelo time informado enquanto visitante## 
def gravaTime_visitanteCampeao(nomeArquivo, campeonato, time):
    arquivo = open(nomeArquivo, "+w", encoding = 'UTF-8')
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

    
def grafico(nomeArquivoVitorias, nomeArquivoDerrotas, time):
    arquivoVitorias = open(nomeArquivoVitorias, "r", encoding = 'UTF-8')
    arquivoDerrotas = open(nomeArquivoDerrotas, "r", encoding = 'UTF-8')
    tamanhoVitorias = arquivoVitorias.readlines()
    tamanhoDerrotas = arquivoDerrotas.readlines()
    contVitorias = 0
    contDerrotas = 0
    time = time.capitalize()
    
    while(len(tamanhoVitorias) > contVitorias):
        contVitorias += 1
        
    while(len(tamanhoDerrotas) > contDerrotas):
        contDerrotas += 1
          
    total = contDerrotas + (contVitorias - 1) #contVitorias tem uma linha a mais por conta do titulo das colunas
    
    if contVitorias==0 or contDerrotas==0:
        print("O time não foi encontrado, por favor, verifique a ortografia do nome.")    
        return 0
    else:
        percentVitorias = float((contVitorias - 1) * 100 / total)
        percentDerrotas = float(contDerrotas * 100 / total)
    
        altura = [percentVitorias, percentDerrotas]
        largura = [0.2,0.2]
        x_pos = [0,0.3]
        barras = ('% Vitórias '+time, '% Derrotas '+time)

        plt.bar(x_pos, altura, largura, color=['blue', 'red'])
        plt.xticks(x_pos, barras)
        plt.show()
        print("Gráfico Ok!")
    
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
file_name2 = "jogos"+time+"Perdeu.txt" #será utilizado para a geração do gráfico
file_name3 = time+"_vitorias.txt" #será utilizado para a geração do gráfico
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
#Gerando a planilha e o txt de vitorias
if os.stat(time+"_visitanteCampeao.txt").st_size == 0 and os.stat(time+"_mandanteCampeao.txt").st_size == 0:
    print("Não foi possível gerar a planilha, pois o time informado não foi encontrado no arquivo original, verifique a grafia correta do nome do time!")
else:
    df_mesclado_vitorias.reset_index(drop=True).to_excel(file_name)
    df_mesclado_vitorias.reset_index(drop=True).to_csv(file_name3)
    #Cria Gráfico
    grafico(file_name3, file_name2, time)
    print("Planilha Ok!")

##REmove arquivos desnecessários##
if os.path.isfile(file_name2):
    os.remove(file_name2)
else:
    print("Erro ao remover %s, o arquivo não existe" %file_name2)
    
if os.path.isfile(file_name3):
    os.remove(file_name3)
else:    ## Show an error ##
    print("Erro ao remover %s, o arquivo não existe" %file_name3)

if os.path.isfile("mandantesCampeoes.txt"):
    os.remove("mandantesCampeoes.txt")
else:    ## Show an error ##
    print("Erro ao remover mandantesCampeoes.txt, o arquivo não existe")
    
if os.path.isfile("visitantesCampeoes.txt"):
    os.remove("visitantesCampeoes.txt")
else:    ## Show an error ##
    print("Erro ao remover visitantesCampeoes.txt, o arquivo não existe")
 
if os.path.isfile("jogosUp.txt"):
    os.remove("jogosUp.txt")
else:    ## Show an error ##
    print("Erro ao remover jogosUp.txt, o arquivo não existe")
   
if os.path.isfile(time+"_mandanteCampeao.txt"):
    os.remove(time+"_mandanteCampeao.txt")
else:    ## Show an error ##
    print("Erro ao remover %s_mandanteCampeao.txt, o arquivo não existe" %time)
    
if os.path.isfile(time+"_visitanteCampeao.txt"):
    os.remove(time+"_visitanteCampeao.txt")
else:    ## Show an error ##
    print("Erro ao remover %s_visitanteeCampeao.txt, o arquivo não existe" %time)