import requests

BASE_URL = 'https://api.mangadex.org'

def search_manga_by_title(title:str) -> list[dict]:
    try:
        payload = {
            'title':title,
            'contentRating[]': ['safe', 'suggestive']
        }
        return requests.get(f'{BASE_URL}/manga', params=payload).json()['data']
    except Exception as e:
        print(f'Erro ao pesquisar mangás: {e}')
        return []
# if __name__ == '__main__':
    # import json

    # with open('search.json', 'w') as fw:
    #     json.dump(search_manga_by_title('one piece'), fw, indent=4)