from flask import render_template, url_for, request
from . import manga_bp
from app.api import Manga


@manga_bp.route("/<manga_id>/chapter/<chapter_number>")
def read_chapter(manga_id:str, chapter_number:str):
    language = request.args.get('language')
    manga = Manga(manga_id)

    if language:
        chapter = manga.get_chapter_athome_data(chapter_number, language)
    else:
        chapter = manga.get_chapter_athome_data(chapter_number)
    
    return render_template('chapter.html', chapter=chapter)
