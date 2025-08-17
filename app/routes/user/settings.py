from flask import redirect, url_for, request, render_template, flash, get_flashed_messages
from flask_login import login_required, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User, UserSettings
from app import db

from . import user_bp

@user_bp.route('/settings')
@login_required
def settings():
    user_settings:UserSettings = UserSettings.query.filter_by(user_id=current_user.id).first()
    content_ratings = {
        'safe':user_settings.safe,
        'suggestive':user_settings.suggestive,
        'erotica':user_settings.erotica,
        'pornographic':user_settings.pornographic
    }

    return render_template('settings/settings.html', filters=content_ratings)

@user_bp.route('/settings/update', methods = ['POST'])
@login_required
def update_settings():
    safe = bool(request.form.get('safe'))
    suggestive = bool(request.form.get('suggestive'))
    erotica = bool(request.form.get('erotica'))
    pornographic = bool(request.form.get('pornographic'))

    user_settings:UserSettings = UserSettings.query.filter_by(user_id=current_user.id).first()
    if user_settings.safe != safe:
        user_settings.safe = safe
    if user_settings.suggestive != suggestive:
        user_settings.suggestive = suggestive
    if user_settings.erotica != erotica:
        user_settings.erotica = erotica
    if user_settings.pornographic != pornographic:
        user_settings.pornographic = pornographic
    db.session.commit()

    return redirect(url_for('index.index'))

@user_bp.route('/settings/password', methods = ['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        password = request.form.get('password')
        new_passwords = [request.form.get('new-password-1'), request.form.get('new-password-2')]

        if not check_password_hash(current_user.password_hash, password):
            flash('A senha atual está incorreta', 'error')
        if new_passwords[0] != new_passwords[1]:
            flash('As novas senhas não correspondem uma com a outra','error')
        if password == new_passwords[0] or password == new_passwords[1]:
            flash('Sua nova senha não pode ser igual a atual','error')

        if not get_flashed_messages(category_filter='error'):
            user:User = User.query.get(current_user.id)
            print(user)
            user.password_hash = generate_password_hash(new_passwords[0])
            
            db.session.commit()

            return redirect(url_for('user.settings'))
        
    return render_template('settings/password.html')

@user_bp.route('/settings/delete-account', methods = ['GET', 'POST'])
@login_required
def delete():
    if request.method == 'POST':
        confirm_message = request.form.get('confirm-message')

        if confirm_message.lower() == 'tenho certeza':
            user:User = User.query.get(current_user.id)
            db.session.delete(user)
            db.session.commit()

            logout_user()

            return redirect(url_for('index.index'))
        else:
            flash('Digite a mensagem informada', 'error')    
    return render_template('settings/delete.html')
