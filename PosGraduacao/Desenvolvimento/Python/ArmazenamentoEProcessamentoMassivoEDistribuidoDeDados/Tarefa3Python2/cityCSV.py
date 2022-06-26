'''
Created on 14 de jun. de 2022

@author: daline
'''
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='sakila', user='root', password='MySQL_2022')

def gerar_excel_json():
    sql_query = pd.read_sql_query ('''
                                   SELECT country as Pais, city as Cidade FROM city  INNER JOIN country ON city.country_id =country.country_id order by city.city  ;
                                   ''', conn)
    df = pd.DataFrame(sql_query, columns=['Cidade', 'Pais'])
    df.to_excel('Cidade.xlsx', index = False)
    df.to_json('Cidade.json', orient='records')
    print("Fim do Processamento ....")

gerar_excel_json()
