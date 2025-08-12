from flask import Blueprint, redirect, url_for, current_app, request, render_template
from flask_login import login_required, current_user

from app.models import user, UserLibrary
from app import db

lib_bp = Blueprint('library', __name__, url_prefix='/library')

@login_required
@lib_bp.route('/')
def library_view():
    library:list[UserLibrary] = UserLibrary.query.filter_by(user_id=current_user.id).all()
    
    library_list = []
    for row in library:
        library_list.append(row.manga_id)
    
    return render_template('library.html', library_list=library_list)

@login_required
@lib_bp.route('/add', methods = ['POST'])
def add_to_library():
    print(request.form.keys())

    keys = list(request.form.keys())
    manga_id = keys[0]

    with current_app.app_context():
        db.session.add(UserLibrary(manga_id=manga_id, user_id=current_user.id))
        db.session.commit()
        
    return redirect(url_for('library.library_view'))