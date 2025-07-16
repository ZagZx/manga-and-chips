import requests
from typing import Union

class Manga:
    BASE_URL = 'https://api.mangadex.org'
    BASE_UPLOADS_URL = 'https://uploads.mangadex.org'

    def __init__(self, manga_id:str):
        self.manga_id = manga_id
        self._cover_id = None
        self._manga_data = None

    @property
    def manga_data(self) -> Union[dict, None]:
        if not self._manga_data:
            try:
                self._manga_data = requests.get(f'{self.BASE_URL}/manga/{self.manga_id}')
                self._manga_data = self._manga_data.json()['data']
            except Exception as e:
                print(f'Erro ao buscar os dados do mangá: {e}')
        return self._manga_data
    
    @property
    def cover_id(self) -> Union[str, None]:
        if not self._cover_id:
            try:
                for relation in self.manga_data['relationships']:
                    if relation['type'] == 'cover_art':
                        self._cover_id = relation['id']

                if not self._cover_id:
                    raise Exception('id não encontrado')
            except Exception as e:
                print(f'Erro ao buscar id da cover: {e}')
        return self._cover_id

    def get_cover_image(self):
        pass

if __name__ == '__main__':
    jojo = Manga('1044287a-73df-48d0-b0b2-5327f32dd651')

    print(jojo.cover_id)