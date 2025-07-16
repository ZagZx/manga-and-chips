from flask import Flask, render_template, Response, request, url_for
from flask_login import login_user,logout_user,current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

from os import getenv
import requests

# load_dotenv('./.env')

app = Flask(__name__)
# app.secret_key = getenv('SECRET_KEY')

@app.route('/')
def index():
    # manga_id = '1044287a-73df-48d0-b0b2-5327f32dd651'
    # filename = 'e7e5e267-502f-4b77-9f19-b7ea1344f68f.jpg'
    
    
    # headers = {'Referer':'https://mangadex.org'}

    # request = requests.get(url,headers=headers)
    # Response(request.content, content_type=request.headers['Content-Type'])
    return render_template('index.html')

@app.route('/cover-proxy')
def cover_proxy():
    manga_id = request.args.get('manga_id')
    filename = request.args.get('filename')

    if filename and manga_id:

        url = f'https://uploads.mangadex.org/covers/{manga_id}/{filename}'
        response = requests.get(url)

        return response.content
    