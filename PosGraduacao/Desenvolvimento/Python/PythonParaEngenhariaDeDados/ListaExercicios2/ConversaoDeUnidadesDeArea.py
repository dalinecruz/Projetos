# -*- coding: iso-8859-1 -*-
'''
Created on 3 de mai. de 2022

@author: daline
'''

class ConversaoDeUnidadesDeArea:

    @staticmethod
    def metroPe(metro):
        pe = metro*10.76
        return pe
    
    @staticmethod
    def peCm(pe):
        cm = pe*929
        return cm
    
    @staticmethod
    def milhaAcre(milha):
        acre = milha*640
        return acre
    
    @staticmethod
    def acrePe(acre):
        pe = acre*43.560
        return pe