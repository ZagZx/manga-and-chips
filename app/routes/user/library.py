from flask import redirect, url_for, current_app, request, render_template
from flask_login import login_required, current_user

from app.models import UserLibrary
from app import db

from . import user_bp


@user_bp.route('/library')
@login_required
def library_view():
    library:list[UserLibrary] = UserLibrary.query.filter_by(user_id=current_user.id).all()
    
    library_list = []
    for row in library:
        library_list.append(row.manga_id)
    
    return render_template('library.html', library_list=library_list)


@user_bp.route('/library/add', methods = ['POST'])
@login_required
def add_to_library():
    print(request.form.keys())

    keys = list(request.form.keys())
    manga_id = keys[0]

    with current_app.app_context():
        db.session.add(UserLibrary(manga_id=manga_id, user_id=current_user.id))
        db.session.commit()
        
    return redirect(url_for('user.library_view'))

@user_bp.route('/library/remove', methods = ['POST'])
@login_required
def remove_from_library():
    keys = list(request.form.keys())
    manga_id = keys[0]

    row = UserLibrary.query.filter_by(user_id=current_user.id, manga_id=manga_id).first()
    print(row)
    with current_app.app_context():
        try:        
            db.session.delete(row)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            db.session.remove()
    return redirect(url_for('user.library_view'))