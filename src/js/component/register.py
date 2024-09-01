from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

def connect_to_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1d0ntw4nn4kn0w",
            database="file_manager_eco"
        )
        if db.is_connected():
            print("Conexión exitosa a la base de datos")
        return db
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirmpassword = data.get('confirmpassword')

    if not all([username, email, password, confirmpassword]):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    if password != confirmpassword:
        return jsonify({"message": "Las contraseñas no coinciden"}), 400

    db = connect_to_db()
    if db is None:
        return jsonify({"message": "Error al conectar a la base de datos"}), 500

    try:
        cursor = db.cursor()
        sql = "INSERT INTO users (username, email, password, confirmpassword) VALUES (%s, %s, %s, %s)"
        val = (username, email, password, confirmpassword)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except Error as e:
        print(f"Error al insertar datos: {e}")
        return jsonify({"message": f"Error al insertar datos: {e}"}), 500
    finally:
        db.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    db = connect_to_db()
    if db is None:
        return jsonify({"message": "Error al conectar a la base de datos"}), 500

    try:
        cursor = db.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        val = (email, password)
        cursor.execute(sql, val)
        user = cursor.fetchone()
        cursor.fetchall()  # Leer todos los resultados para evitar el error "Unread result found"
        cursor.close()

        if user:
            return jsonify({"message": "Inicio de sesión exitoso", "redirect_url": url_for('welcome')}), 200
        else:
            return jsonify({"message": "Correo electrónico o contraseña incorrectos"}), 401
    except Error as e:
        print(f"Error al consultar datos: {e}")
        return jsonify({"message": f"Error al consultar datos: {e}"}), 500
    finally:
        db.close()

@app.route('/welcome')
def welcome():
    return "Bienvenido a la página de bienvenida"

if __name__ == '__main__':
    app.run(debug=True)
