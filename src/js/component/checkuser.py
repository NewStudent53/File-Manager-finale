from flask import Flask, request, redirect, session, render_template_string
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Reemplaza con tu clave secreta

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'your_database_name'  # Reemplaza con el nombre de tu base de datos
}

# Conectar a la base de datos
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

@app.route('/signIn', methods=['POST'])
def sign_in():
    email = request.form['email']
    password = hashlib.md5(request.form['password'].encode()).hexdigest()

    cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
    user = cursor.fetchone()

    if user:
        session['email'] = user['email']
        return redirect('/dashboard')
    else:
        return render_template_string("<script>alert('No encontrado, correo o contraseña incorrectos');window.location.href='/';</script>")

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        return f'Bienvenido al panel de control, {session["email"]}'
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
