from flask import redirect, url_for, current_app, request, render_template
from flask_login import login_required, current_user

from app.models import UserLibrary
from app import db
from app.api import Manga

from . import user_bp


@user_bp.route('/library')
@login_required
def library_view():
    library:list[UserLibrary] = UserLibrary.query.filter_by(user_id=current_user.id).all()
    
    mangas = []

    # isso trava a rota porque toda vez que chama o manga.title
    # solução: enviar apenas o ID do mangá para o HTML, e lá, ter um url_for para uma rota que pega os dados do mangá 
    # fazer um lazy loading com javascript
    for row in library:
        
        manga = Manga(row.manga_id) 

        mangas.append({
            'id':manga.id,
            'title':manga.title,
            'cover_image': url_for('proxy.cover', manga_id=manga.id, filename=manga.cover_filename)
        })
    
    return render_template('library.html', mangas=mangas)

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
    db.session.delete(row)
    db.session.commit()

    return redirect(url_for('user.library_view'))