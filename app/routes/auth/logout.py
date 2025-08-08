from . import auth_bp
from flask_login import login_required, logout_user
from flask import redirect, url_for


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('index'))