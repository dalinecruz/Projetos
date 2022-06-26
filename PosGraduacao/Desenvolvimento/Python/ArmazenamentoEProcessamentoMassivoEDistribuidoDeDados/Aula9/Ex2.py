# -*- coding: iso-8859-1 -*-
'''
Created on 7 de jun. de 2022

@author: daline
'''
import pandas as pd

df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})

print(df)

print(df)
print(df.columns)
print(df["Seminário"])
print(df.describe())
print(df.sort_values(by="Seminário"))
file_name = 'DataFrame.xlsx'
  
# saving the excel
df.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')