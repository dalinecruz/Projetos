# -*- coding: iso-8859-1 -*-
'''
Created on 3 de mai. de 2022

@author: daline
'''
from ListaExercicios2.ConversaoDeUnidadesDeArea import ConversaoDeUnidadesDeArea
opcao = 0

while True:
    opcao = int(input("\nConversão de medidas \n" 
                      + "\n1) Converter m² em pé² " + "\n" 
                      + "2) Converter pé² em cm² " + "\n" 
                      + "3) Converter mi² em acre " + "\n"
                      + "4) Converta acre em pé² " + "\n"  
                      + "5) Sair\n" ))

    if opcao > 5 or opcao < 1:
        print("Opcao Invalida! ")
        continue
    
    if(opcao == 5):
        print('Programa encerrado!')
        break
   
    if(opcao == 1):
        print('Total de {} pé².'.format(ConversaoDeUnidadesDeArea.metroPe(int(input('\nInsira a quantidade de metro²: ')))))
    
    if(opcao == 2):
        print('Total de {} cm².'.format(ConversaoDeUnidadesDeArea.peCm(int(input('\nInsira a quantidade de pé²: ')))))
        
    if(opcao == 3):
        print('Total de {} acres.'.format(ConversaoDeUnidadesDeArea.milhaAcre(int(input('\nInsira a quantidade de mi²: ')))))
        
    if(opcao == 4):
        print('Total de {} pé².'.format(ConversaoDeUnidadesDeArea.acrePe(int(input('\nInsira a quantidade de acres: ')))))
