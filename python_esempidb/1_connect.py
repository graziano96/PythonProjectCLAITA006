# Connessione a un database MySQL
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password", 
    database="scuola"
)

print("Connessione avvenuta con successo!")

conn.close()
