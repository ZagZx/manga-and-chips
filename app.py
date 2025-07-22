from flask import Flask, render_template, Response, request, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

import os
import requests

from database import Database
from models import User

DB_PATH = './database/database.db'
SQL_PATH = './database/schema.sql'

db = Database(DB_PATH)

DROPAR_TABELAS = False
# evitar drop das tabelas toda vez que rodar o codigo
if not os.path.exists(DB_PATH) or DROPAR_TABELAS:
    db.run_sql_file(SQL_PATH) # cria as tabelas | COLOCAR ISSO NO build.py DEPOIS

load_dotenv('./.env')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    user_data = db.run_query('SELECT id, username, email FROM users WHERE id = ?', user_id)[0]
    if user_data:
        return User(id=user_data[0], username=user_data[1], email=user_data[2])
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password_hash = generate_password_hash(request.form.get('password'))

        if not db.run_query(f"SELECT * FROM users WHERE email = ?", email):
            db.run_query(f"INSERT INTO users(username, email, password_hash) VALUES (?, ?, ?)", (username, email, password_hash))
            return redirect(url_for('login'))
        else: 
            print('Já existe um usuário cadastrado com esse email')
            return render_template('register.html') # colocar mensagem de erro
    if request.method == 'GET':
        return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # fazer tratamento de erros caso a senha esteja errada
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_data = db.run_query('SELECT id, username, password_hash FROM users WHERE email = ?', (email,))[0]
        print(user_data[0])
        if user_data and check_password_hash(user_data[2], password):
            user = User(id=user_data[0], username=user_data[1], email=email)
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html') # colocar mensagem de erro
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('index'))

@app.route('/cover-proxy')
def cover_proxy():
    manga_id = request.args.get('manga_id')
    filename = request.args.get('filename')

    if filename and manga_id:
        url = f'https://uploads.mangadex.org/covers/{manga_id}/{filename}'
        response = requests.get(url)

        return Response(response.content, content_type=response.headers['Content-Type'])