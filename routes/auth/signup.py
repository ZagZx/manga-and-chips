from flask import request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
from . import auth_bp

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
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