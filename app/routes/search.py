from flask import url_for, render_template, request, Blueprint
from flask_login import current_user

from app.api import search_manga_by_title, Manga
from app.models import UserLibrary


search_bp = Blueprint('search', __name__)

@search_bp.route('/search')
def search():
    title = request.args.get('query')
    results = search_manga_by_title(title)
    
    # import json 
    # with open('manga_data.json', 'w') as fw:
    #     json.dump(results, fw, indent=4)

    mangas_list = []
    for manga_data in results:
        manga = Manga(manga_data['id'])
        manga.manga_data = manga_data
        # print(manga.cover_data.keys())
        # print(manga.cover_data['attributes']['fileName'])
        print(manga.title)
        print(manga.cover_filename)
        # print(manga.cover_id)

        mangas_list.append(
            {
                "id": manga.id,
                "title": manga.title,
                # vai travar o site se for via request, mas se for via busca no dicionario ta de boa
                "cover_image": url_for('proxy.cover', manga_id = manga.id, filename=manga.cover_filename)
            }
        )
    
    library = []
    if current_user.is_authenticated:
        user_library:list[UserLibrary] = UserLibrary.query.filter_by(user_id=current_user.id).all()
        for manga in user_library:
            library.append(manga.manga_id)
        

    return render_template('search.html', mangas_list = mangas_list, library=library)
