from email import message
from flask import Flask, render_template, request, redirect, url_for, session
from model.model_user import Usuario
from datetime import datetime
from app import app
from model.database_manager import DatabaseManager
from view import *

db = DatabaseManager()
@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        try:
            data = {
                'id_usuario': request.form['idusuario'],
                'contrasena': request.form['contrasena'],
                'edad': request.form['edad'],
                'nombre_usuario': request.form['nombre_usuario'],
                'genero': request.form['genero']
            }
            
            if Usuario.create('usuario', data):
                return redirect(url_for('login_user'))
            else:
                return render_template('register.html', title='Registro', message='Error al crear el usuario. Intente nuevamente.', year=datetime.now().year)
        except Exception as e:
            print(f"Error en el formulario de registro: {e}")
            return render_template('register.html', title='Registro', message='Error en el formulario de registro. Intente nuevamente.', year=datetime.now().year)
    
    return render_template('register.html', title='Registro', message='Por favor, complete el formulario de registro.', year=datetime.now().year)

@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        id_usuario = request.form['idusuario']
        contrasena = request.form['contrasena']
        
        usuario = Usuario.find_by_credentials(id_usuario, contrasena)
        
        if usuario:
            session['logged_in'] = True
            session['id_usuario'] = id_usuario
            return redirect(url_for('session_home'))
        else:
            return render_template('login.html', title='Inicia Sesion', year=datetime.now().year, error='ID de usuario o contrasena incorrectos.')
    
    return render_template('login.html', title='Inicia Sesion', year=datetime.now().year)
