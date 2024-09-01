import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',  # Reemplaza con tu contraseña
    database='your_database_name'  # Reemplaza con el nombre de tu base de datos
)

cursor = conn.cursor(dictionary=True)
