from flask import redirect, url_for, current_app, request, render_template
from flask_login import login_required, current_user

from app.models import UserLibrary
from app import db

from . import user_bp

@user_bp.route('/settings')
def settings():
    return render_template('settings.html')