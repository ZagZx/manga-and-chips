from flask import url_for, render_template, request, Blueprint
from api import search_manga_by_title, Manga

search_bp = Blueprint('pesquisa', __name__, url_prefix='/pesquisa')

@search_bp.route('/pesquisa')
def search():
    title = request.args.get('query')
    results = search_manga_by_title(title)

    mangas_list = []
    for manga_data in results:
        manga = Manga(manga_data['id'])
        manga.manga_data = manga_data

        mangas_list.append(
            {
                "id": manga.id,
                "title": manga.title,
                "cover_image": url_for('cover_proxy_by_manga_id', manga_id = manga.id)
            }
        )

    return render_template('search.html', mangas_list = mangas_list)
