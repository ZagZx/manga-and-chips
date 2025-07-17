import requests
from typing import Union

class Manga:
    BASE_URL = 'https://api.mangadex.org'
    BASE_UPLOADS_URL = 'https://uploads.mangadex.org'

    def __init__(self, manga_id:str):
        self.manga_id = manga_id
        self._manga_data = None
        self._cover_id = None
        self._cover_filename = None
        self._cover_image = None

    @property
    def manga_data(self) -> Union[dict, None]:
        if not self._manga_data:
            try:
                response = requests.get(f'{self.BASE_URL}/manga/{self.manga_id}')
                self._manga_data = response.json()['data']
            except Exception as e:
                print(f'Erro ao buscar os dados do mangá: {e}')
        return self._manga_data
    
    @property
    def cover_id(self) -> Union[str, None]:
        if not self._cover_id:
            try:
                if not self.manga_data:
                    raise Exception('Não foi possível obter manga_data')
                # vai pegar a primeira cover art que encontrar, tem alguma cover que seja melhor que outra?
                for relation in self.manga_data['relationships']: 
                    if relation['type'] == 'cover_art':
                        self._cover_id = relation['id']
                        break

                if not self._cover_id:
                    raise Exception('id não encontrado')
            except Exception as e:
                print(f'Erro ao buscar id da cover: {e}')
        return self._cover_id

    @property
    def cover_filename(self) -> Union[str, None]:
        if not self._cover_filename:
            try:
                if not self.cover_id:
                    raise Exception('Não foi possível obter o cover_id')
                response = requests.get(f'{self.BASE_URL}/cover/{self.cover_id}')
                self._cover_filename = response.json()['data']['attributes']['fileName']
            except Exception as e:
                print(f'Erro ao buscar o filename da cover: {e}')
        return self._cover_filename
    
    @property
    def cover_image(self) -> Union[bytes, None]:
        if not self._cover_image:
            try:
                if not self.cover_filename:
                    raise Exception('Não foi possível obter o cover_filename')
                response = requests.get(f'{self.BASE_UPLOADS_URL}/covers/{self.manga_id}/{self.cover_filename}')
                self._cover_image = response.content
            except Exception as e:
                print(f'Erro ao buscar a imagem da cover_art: {e}')
        return self._cover_image    
if __name__ == '__main__':
    jojo = Manga('1044287a-73df-48d0-b0b2-5327f32dd651')
    print(jojo.cover_image)