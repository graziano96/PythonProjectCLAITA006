# Selezione e stampa di tutti i record
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="scuola"
) 

cursor = conn.cursor()

cursor.execute("SELECT * FROM studenti")
risultati = cursor.fetchall()

for (id, nome, voto) in risultati:
    print(f"{id} - {nome} - {voto}")

cursor.close()
conn.close()
