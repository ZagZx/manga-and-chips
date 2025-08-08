from flask import Flask
from flask_login import LoginManager

from dotenv import load_dotenv
import os

from models import db, User, UserLibrary

from routes.auth import auth_bp
from routes.manga import manga_bp
from routes.proxy import proxy_bp
from routes.index import index_bp
from routes.search import search_bp

load_dotenv('./.env')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
with app.app_context():
    db.create_all()

    # from werkzeug.security import generate_password_hash
    # db.session.add(User(username='ZagZ', email='zezi@example.com', password_hash=generate_password_hash('123')))
    # db.session.commit()

    # user:User = User.query.get(1)
    # print('\n',user.id, user.username, user.email, '\n')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.register_blueprint(auth_bp)
app.register_blueprint(manga_bp)
app.register_blueprint(proxy_bp)
app.register_blueprint(index_bp)
app.register_blueprint(search_bp)
