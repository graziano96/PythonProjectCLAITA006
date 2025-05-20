# Eliminazione di un record
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="scuola"
)
 
cursor = conn.cursor()

sql = "DELETE FROM studenti WHERE nome = %s"
valori = ("Giulia",)

cursor.execute(sql, valori)
conn.commit()

print(f"{cursor.rowcount} record eliminato.")

cursor.close()
conn.close()
