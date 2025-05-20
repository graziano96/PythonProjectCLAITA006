# Aggiornamento di un record esistente
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="scuola"
) 

cursor = conn.cursor()

sql = "UPDATE studenti SET voto = %s WHERE nome = %s"
valori = (30, "Giulia")

cursor.execute(sql, valori)
conn.commit()

print(f"{cursor.rowcount} record aggiornato.")

cursor.close()
conn.close()
