import mysql.connector
from mysql.connector import Error
import json

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1d0ntw4nn4kn0w",
        database="file_manager_eco"
    )
    if db.is_connected():
        print("Conexión exitosa a la base de datos")
except Error as e:
    print(f"Error al conectar a la base de datos: {e}")

# Datos de prueba en formato JSON
data = {
    "username": "guillermo",
    "email": "testuser@example.com",
    "password": "password123",
    "confirmpassword": "password123"
}

# Convertir el diccionario de Python a una cadena JSON
json_data = json.dumps(data)
print("Datos JSON:", json_data)

# Insertar los datos en la base de datos
try:
    cursor = db.cursor()
    sql = "INSERT INTO users (username, email, password, confirmpassword) VALUES (%s, %s, %s, %s)"
    val = (data['username'], data['email'], data['password'], data['confirmpassword'])
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    print("Usuario registrado exitosamente")
except Error as e:
    print(f"Error al insertar datos: {e}")
