import sqlite3 as sql

connection = sql.connect("database.db")

cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS dados (
               ID INTEGER PRIMARY KEY AUTOINCREMENT
               MOEDA_ID INTEGER
               DIA_COTACAO INTEGER
               NOME_MOEDA TEXT
               )''')