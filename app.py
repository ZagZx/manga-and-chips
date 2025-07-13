from flask import Flask
from flask_login import login_user,logout_user,current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

from os import getenv

load_dotenv('./.env')

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')