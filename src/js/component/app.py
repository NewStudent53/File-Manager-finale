import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify

app = Flask(__name__)

# Conexión a la base de datos
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1D0ntw4nn4kn@w",
        database="sys"
    )
    if db.is_connected():
        print("Conexión exitosa a la base de datos")
except Error as e:
    print(f"Error al conectar a la base de datos: {e}")

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        confirmpassword = data['confirmpassword']

        cursor = db.cursor()
        sql = "INSERT INTO users (username, email, password, confirmpassword) VALUES (%s, %s, %s, %s)"
        val = (username, email, password, confirmpassword)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
