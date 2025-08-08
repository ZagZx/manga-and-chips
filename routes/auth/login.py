from flask import request, redirect, url_for, render_template
from flask_login import login_user
from models import User
from werkzeug.security import check_password_hash
from . import auth_bp


@auth_bp.route('/login', methods = ['GET', 'POST'])
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
    
