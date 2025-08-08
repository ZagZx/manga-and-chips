from flask import redirect, url_for, Response
from time import time

from app.api import Manga
from . import proxy_bp


@proxy_bp.route('/cover/<manga_id>/<filename>')
def cover_proxy(manga_id:str, filename:str):
    before = time()
    
    manga = Manga(manga_id)

    if filename and manga_id:
        cover_image = manga.cover_image

        now = time()
        print('\n====COVER PROXY====')
        print(f'Mangá: {manga.title}')
        print(f'Tempo de Execução: {round(now-before,2)}s\n')

        return Response(cover_image.content, content_type=cover_image.headers['Content-Type'])
    
@proxy_bp.route('/cover/<manga_id>')
def cover_proxy_by_manga_id(manga_id):
    '''
    Gambiarra para acelerar a pesquisa, ao invés de passar os filenames e travar a página por muito tempo,
    é passado no dicionário um url_for para esta rota e nela é obtido o filename e então ela redireciona para a cover_proxy.

    Ou seja, aumenta o tempo de carregamento das imagens para diminuir consideravelmente o tempo de tela travada.
    '''

    manga = Manga(manga_id)
    cover_filename = manga.cover_filename
    return redirect(url_for('proxy.cover_proxy', manga_id = manga_id, filename = cover_filename))