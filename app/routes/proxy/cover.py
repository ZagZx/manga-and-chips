from flask import redirect, url_for, Response, request
from time import time

from app.api import Manga
from app.api import get_cover_image
from . import proxy_bp


@proxy_bp.route('/cover/<manga_id>/<filename>')
def cover(manga_id:str, filename:str):
    before = time()

    if filename and manga_id:
        cover_image = get_cover_image(manga_id, filename)        

        now = time()
        print('\n====COVER PROXY====')
        print(manga_id)
        # print(f'Mangá: {manga.title}')
        print(f'Tempo de Execução: {round(now-before,2)}s\n')

        time24h = 86400
        headers = {
            'Content-Type':cover_image.headers['content-type'],
            'Cache-Control':f'public, max-age={time24h}', # guarda a imagem da cover em cache por 24 horas,
            'X-Content-Type-Options': 'nosniff', 
            'X-Frame-Options': 'DENY'
        }

        # print()
        # print(cover_image.headers)
        # print()

        return Response(cover_image.content, headers=headers)

# @proxy_bp.route('/cover/<manga_id>')
# def cover_by_manga_id(manga_id):
#     '''
#     Gambiarra para acelerar a pesquisa, ao invés de passar os filenames e travar a página por muito tempo,
#     é passado no dicionário um url_for para esta rota e nela é obtido o filename e então ela redireciona para a cover_proxy.

#     Ou seja, aumenta o tempo de carregamento das imagens para diminuir consideravelmente o tempo de tela travada.
#     '''

#     manga = Manga(manga_id)
#     cover_filename = manga.cover_filename
#     return redirect(url_for('proxy.cover', manga_id = manga_id, filename = cover_filename))