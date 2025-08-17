from flask import url_for, render_template, request, Blueprint
from app.api import search_manga_by_title, Manga

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

    return render_template('search.html', mangas_list = mangas_list)
