import requests
from typing import Union

BASE_URL = 'https://api.mangadex.org'
BASE_UPLOADS_URL = 'https://uploads.mangadex.org'
# CONTENT_RATING = ['safe', 'suggestive']
# INCLUDES = ['cover_art']

DEFAULT_PAYLOAD = {
    'includes[]': 'cover_art',
    'contentRating[]': ['safe', 'suggestive'],
}

def search_manga_by_title(title:str) -> list[dict]:
    try:
        payload = DEFAULT_PAYLOAD.copy()
        payload['title'] = title

        return requests.get(f'{BASE_URL}/manga', params=payload).json()['data']
    except Exception as e:
        print(f'Erro ao pesquisar mangás: {e}')
        return []

def get_last_uploaded_mangas(limit:int):
    try:
        payload = DEFAULT_PAYLOAD.copy()
        payload['order[latestUploadedChapter]'] = 'asc'

        return requests.get(f'{BASE_URL}/manga', params=payload).json()['data']
    except Exception as e:
        print(f'Erro ao pesquisar mangás: {e}')
        return []
    
def get_cover_image(manga_id: str, filename:str) -> requests.Response:
    response = requests.get(f'{BASE_UPLOADS_URL}/covers/{manga_id}/{filename}')
    if response.status_code not in (200, 304): # 304, not modified
        print(f'Erro ao buscar a imagem da cover_art: {response.status_code, response.reason}')
    return response
    
if __name__ == '__main__':
    # print(search_manga_by_title('jojo'))
    # import json

    # with open('search.json', 'w') as fw:
    #     json.dump(search_manga_by_title('one piece'), fw, indent=4)

    pass
