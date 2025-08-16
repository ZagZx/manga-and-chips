from flask import request, redirect, url_for, render_template, current_app
from werkzeug.security import generate_password_hash

from . import auth_bp
from app.models import User, UserSettings
from app import db

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password_hash = generate_password_hash(request.form.get('password'))

        if User.query.filter_by(email=email).first():
            print('Já existe um usuário cadastrado com esse email')
            return render_template('register.html') # colocar mensagem de erro

        else: 
            user:User = User(username=username, email=email, password_hash=password_hash)
            db.session.add(user)
            db.session.flush()
            db.session.add(UserSettings(user_id=user.id))
            db.session.commit()
            
            return redirect(url_for('auth.login'))
    if request.method == 'GET':
        return render_template('register.html')