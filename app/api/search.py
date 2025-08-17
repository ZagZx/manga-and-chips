import requests
from typing import Union

BASE_URL = 'https://api.mangadex.org'
BASE_UPLOADS_URL = 'https://uploads.mangadex.org'
# CONTENT_RATING = ['safe', 'suggestive']
# INCLUDES = ['cover_art']

DEFAULT_PAYLOAD = [
    ('includes[]', 'cover_art'),
    ('contentRating[]', 'safe'),
    ('contentRating[]', 'suggestive')
]

def search_manga_by_title(title:str) -> list[dict]:
    try:
        payload = DEFAULT_PAYLOAD.copy()
        payload.append(('title', title))

        return requests.get(f'{BASE_URL}/manga', params=payload).json()['data']
    except Exception as e:
        print(f'Erro ao pesquisar mangás: {e}')
        return []

def get_last_uploaded_mangas(limit:int):
    try:
        payload = DEFAULT_PAYLOAD.copy()
        payload.append(('order[latestUploadedChapter]', 'asc'))

        return requests.get(f'{BASE_URL}/manga', params=payload).json()['data']
    except Exception as e:
        print(f'Erro ao pesquisar mangás: {e}')
        return []
    
def get_cover_image(manga_id: str, filename:str) -> Union[requests.Response, None]:
    cover_image = None
    try:
        response = requests.get(f'{BASE_UPLOADS_URL}/covers/{manga_id}/{filename}')
        cover_image = response
        # self._cover_image = response.content
    except Exception as e:
        print(f'Erro ao buscar a imagem da cover_art: {e}')
    return cover_image
    
if __name__ == '__main__':
    # print(search_manga_by_title('jojo'))
    # import json

    # with open('search.json', 'w') as fw:
    #     json.dump(search_manga_by_title('one piece'), fw, indent=4)

    pass
