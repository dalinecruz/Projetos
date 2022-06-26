'''
Created on 14 de jun. de 2022

@author: daline
'''
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='sakila', user='root', password='MySQL_2022')

sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM actor order by first_name
                               ''', conn)

df = pd.DataFrame(sql_query, columns = ['actor_id', 'first_name', 'last_name', 'last_update'])
file_name = 'Exemplo Pandas SQl.xlsx'
df.to_excel(file_name)
print("ok")