# -*- coding: iso-8859-1 -*-
'''
Created on 10 de mai. de 2022

@author: daline
'''
from Aula6.Elevador import Elevador

e = Elevador()

while True:
    opcao = int(input("\nElevador \n"
                      + "\n1) Iniciar " + "\n"
                      + "2) Entrar no elevador " + "\n" 
                      + "3) Sair do elevador" + "\n" 
                      + "4) Subir" + "\n" 
                      + "5) Descer" +"\n" 
                      + "6) Encerrar\n" ))
    
    
    if opcao > 6 or opcao < 1:
        print("Opcao inválida, tente novamente! ")
        continue
    
    if(opcao == 6):
        print("Elavador parado no andar {} e com lotação de {} pessoas.".format(e.getAndar_atual(), e.getQtde_pessoas()))
        print("Elevador encerrado!")
        break
    
    if (opcao == 1):
        print('Para iniciar o elevador informe os dados abaixo: ')
        e.setCapacidade_elevador(int(input("\nCapacidade total do elevador: ")))
        e.setTotal_andares(int(input("Total de andares do prédio: ")))
        continue
    
    if(opcao == 2):
        capacidade = e.getCapacidade_elevador()
        lotacao = e.getQtde_pessoas()
        if lotacao < capacidade:
            print("Entrou!")
            lotacao += 1
            e.setQtde_pessoas(lotacao)
            print("O elevador está com {} pessoas!".format(lotacao))
        else:
            print("Elevador lotado!")
        continue       
        
    if(opcao == 3):
        capacidade = e.getCapacidade_elevador()
        lotacao = e.getQtde_pessoas()
        if lotacao > 0:
            print("Saiu!")
            lotacao -= 1
            e.setQtde_pessoas(lotacao)
            print("O elevador está com {} pessoas!".format(lotacao))
        else:
            print("O elevador já está vazio!")
        continue

    if(opcao == 4):
        andar_atual = e.getAndar_atual()
        max_andar = e.getTotal_andares()
        print("Você está no andar: ", andar_atual)
        novo_andar = (int(input("Informe o novo andar: ")))
        if (novo_andar > max_andar):
            print("O andar {} não existe e não é possível executar nenhuma ação!".format(novo_andar))
        else:
            if (novo_andar <= andar_atual):
                print("Você já está no andar {}!".format(andar_atual, novo_andar))
            else:
                e.setAndar_atual(novo_andar)
                print("Bem-vindo ao andar {}".format(novo_andar))
                print("")
        continue
        
    if(opcao == 5):
        andar_atual = e.getAndar_atual()
        max_andar = e.getTotal_andares()
        print("Você está no andar: ", andar_atual)
        novo_andar = (int(input("Informe o novo andar: ")))
        if (novo_andar < 0):
            print("O andar {} não existe e não é possível executar nenhuma ação!".format(novo_andar))
        else:
            if (novo_andar >= andar_atual) and (novo_andar <= max_andar):
                print("Você já está no andar {}!".format(andar_atual, novo_andar))
            else:
                if (novo_andar > max_andar):
                    print("O andar {} não existe e não é possível executar nenhuma ação!".format(novo_andar))
                else:
                    e.setAndar_atual(novo_andar)
                    print("Bem-vindo ao andar {}".format(novo_andar))
                    print("")
        continue