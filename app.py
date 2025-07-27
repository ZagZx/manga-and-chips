from flask import Flask, render_template, Response, request, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

import os
import time

from database import Database
from models import User

from utils.api import Manga, search_manga_by_title


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
    user_data = db.run_query('SELECT id, username, email FROM users WHERE id = ?', user_id)
    if user_data:
        user_data = user_data[0]
        return User(id=user_data[0], username=user_data[1], email=user_data[2])
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    title = request.args.get('query')
    results = search_manga_by_title(title)

    mangas_list = []
    for manga_data in results:
        manga = Manga(manga_data['id'])
        manga.manga_data = manga_data
        mangas_list.append(manga)
        # print(manga.title)
    return render_template('search.html', mangas_list = mangas_list)

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

        user_data = db.run_query('SELECT id, username, password_hash FROM users WHERE email = ?', (email,))
        if user_data:
            user_data = user_data[0]
            if check_password_hash(user_data[2], password):
                user = User(id=user_data[0], username=user_data[1], email=email)
                login_user(user)
                return redirect(url_for('index'))
            else:
                print('Senha errada')
        # else:
        #     print('Email não cadastrado')
        return render_template('login.html') # colocar mensagem de erro
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('index'))

@app.route('/cover-proxy/<manga_id>/<filename>')
def cover_proxy(manga_id:str, filename:str):
    before = time.time()
    
    manga = Manga(manga_id)

    if filename and manga_id:
        cover_image = manga.cover_image

        now = time.time()
        print('\n====COVER PROXY====')
        print(f'Mangá: {manga.title}')
        print(f'Tempo de Execução: {round(now-before,2)}s\n')

        return Response(cover_image.content, content_type=cover_image.headers['Content-Type'])