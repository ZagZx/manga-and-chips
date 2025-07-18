from flask import Flask, render_template, Response, request, url_for
from flask_login import login_user,logout_user,current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

import os
import requests

from database import Database

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not db.run_query(f"SELECT * FROM users WHERE email = '{email}'"):
            db.add_user(username, email, password)
        else: 
            print('Já existe um usuário cadastrado com esse email')
        # falta implementar, mas antes terminar a classe Database

    return render_template('register.html')

@app.route('/cover-proxy')
def cover_proxy():
    manga_id = request.args.get('manga_id')
    filename = request.args.get('filename')

    if filename and manga_id:
        url = f'https://uploads.mangadex.org/covers/{manga_id}/{filename}'
        response = requests.get(url)

        return response.content