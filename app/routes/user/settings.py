from flask import redirect, url_for, request, render_template
from flask_login import login_required, current_user

from app.models import UserSettings
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

    return render_template('settings.html', filters=content_ratings)

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