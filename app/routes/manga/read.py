from flask import render_template, url_for
from . import manga_bp
from app.api import Manga



@manga_bp.route("/<manga_id>/chapter/<chapter_number>")
def read_chapter(manga_id:str, chapter_number:str):
    manga = Manga(manga_id)
    chapter = manga.get_chapter_athome_data(chapter_number, 'pt-br')
    
    # print(chapter)
    baseUrl = chapter['baseUrl']
    filename = chapter['chapter']['data'][int(chapter_number)]
    hash = chapter['chapter']['hash']
    print(url_for('chapter_proxy', baseUrl=baseUrl, hash=hash, filename=filename, chapter_number=1))
    
    return render_template('chapter.html', chapter=chapter)
