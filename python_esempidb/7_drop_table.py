# Eliminazione della tabella
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="password",
    database="scuola"
)

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS studenti")

print("Tabella eliminata.")

cursor.close()
conn.close()
