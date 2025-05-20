# Inserimento di un record nella tabella
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="scuola"
) 

cursor = conn.cursor()

sql = "INSERT INTO studenti (nome, voto) VALUES (%s, %s)"
valori = ("Giulia", 27.5)

cursor.execute(sql, valori)
conn.commit()

print(f"{cursor.rowcount} record inserito.")

cursor.close()
conn.close()
