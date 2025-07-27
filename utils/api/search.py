import requests

BASE_URL = 'https://api.mangadex.org'

def search_manga_by_title(title:str) -> list[int]:
    return requests.get(f'{BASE_URL}/manga?title={title}').json()['data']

# if __name__ == '__main__':
    # import json

    # with open('search.json', 'w') as fw:
    #     json.dump(search_manga_by_title('one piece'), fw, indent=4)