from flask import request, redirect, url_for, render_template
from flask_login import login_user
from werkzeug.security import check_password_hash

from . import auth_bp
from app.models import User

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    # fazer tratamento de erros caso a senha esteja errada
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user:User = User.query.filter_by(email=email).first()
        
        if user:
            print(user.id, user.email, user.username)
            
            if check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for('index.index'))
            else:
                print('Senha errada')
        else:
            print('Email não cadastrado')
        return render_template('login.html') # colocar mensagem de erro
    elif request.method == 'GET':
        return render_template('login.html')
    
