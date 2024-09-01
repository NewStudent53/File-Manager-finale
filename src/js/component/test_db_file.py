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
    "user_id": "1",
    "file_name": "testuserexample.txt",
    "file_type": "txt",
    "file_path": "userfiles/user_1/",
    "upload_date": "2024-08-20 21:05:31",
    "trash_indicator": ""
}

# Convertir el diccionario de Python a una cadena JSON
json_data = json.dumps(data)
print("Datos JSON:", json_data)

# Insertar los datos en la base de datos
try:
    cursor = db.cursor()
    sql = "INSERT INTO files (user_id, file_name, file_type, file_path, upload_date, trash_indicator) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (data['user_id'], data['file_name'], data['file_type'], data['file_path'], data['upload_date'], data['trash_indicator'])
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    print("Archivo registrado exitosamente")
except Error as e:
    print(f"Error al insertar datos: {e}")
