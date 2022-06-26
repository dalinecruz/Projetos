# -*- coding: iso-8859-1 -*-
'''
Created on 10 de mai. de 2022

@author: daline
'''

class Elevador():
    
    def __init__(self):
        self.__andar_atual = 0
        self.__total_andares = 0
        self.__capacidade_elevador = 0
        self.__qtde_pessoas = 0
        
    def setAndar_atual(self, andar_atual):
        self.__andar_atual = andar_atual
    
    def getAndar_atual(self):
        return self.__andar_atual
    
    def setTotal_andares(self, total_andares):
        self.__total_andares = total_andares
    
    def getTotal_andares(self):
        return self.__total_andares
    
    def setCapacidade_elevador(self, capacidade_elevador):
        self.__capacidade_elevador = capacidade_elevador
    
    def getCapacidade_elevador(self):
        return self.__capacidade_elevador
    
    def setQtde_pessoas(self, qtde_pessoas):
        self.__qtde_pessoas = qtde_pessoas
    
    def getQtde_pessoas(self):
        return self.__qtde_pessoas    