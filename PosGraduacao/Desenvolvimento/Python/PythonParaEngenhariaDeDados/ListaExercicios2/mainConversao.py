# -*- coding: iso-8859-1 -*-
'''
Created on 3 de mai. de 2022

@author: daline
'''
from ListaExercicios2.ConversaoDeUnidadesDeArea import ConversaoDeUnidadesDeArea
opcao = 0

while True:
    opcao = int(input("\nConvers�o de medidas \n" 
                      + "\n1) Converter m� em p� " + "\n" 
                      + "2) Converter p� em cm� " + "\n" 
                      + "3) Converter mi� em acre " + "\n"
                      + "4) Converta acre em p� " + "\n"  
                      + "5) Sair\n" ))

    if opcao > 5 or opcao < 1:
        print("Opcao Invalida! ")
        continue
    
    if(opcao == 5):
        print('Programa encerrado!')
        break
   
    if(opcao == 1):
        print('Total de {} p�.'.format(ConversaoDeUnidadesDeArea.metroPe(int(input('\nInsira a quantidade de metro�: ')))))
    
    if(opcao == 2):
        print('Total de {} cm�.'.format(ConversaoDeUnidadesDeArea.peCm(int(input('\nInsira a quantidade de p�: ')))))
        
    if(opcao == 3):
        print('Total de {} acres.'.format(ConversaoDeUnidadesDeArea.milhaAcre(int(input('\nInsira a quantidade de mi�: ')))))
        
    if(opcao == 4):
        print('Total de {} p�.'.format(ConversaoDeUnidadesDeArea.acrePe(int(input('\nInsira a quantidade de acres: ')))))
