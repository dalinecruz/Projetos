# -*- coding: iso-8859-1 -*-
'''
Created on 14 de jun. de 2022

@author: daline
'''

import mysql.connector

con = mysql.connector.connect(host='localhost', database='sakila', user='root', password='MySQL_2022')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
