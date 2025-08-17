from flask import request, redirect, url_for, render_template, flash, get_flashed_messages
from flask_login import login_user
from werkzeug.security import check_password_hash

from . import auth_bp
from app.models import User

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user:User = User.query.filter_by(email=email).first()
        
        if user:            
            if check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for('index.index'))
            else:
                flash('Senha incorreta', 'error')
        else:
            flash('O usuário não está cadastrado', 'error')
        return render_template('login.html')
    elif request.method == 'GET':
        return render_template('login.html')