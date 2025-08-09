import requests
from typing import Union

# IF's COMO ESSE SÃO PARA EXIBIR O ERRO BONITINHO NO EXCEPT:
    # if not self.manga_data:
    #     raise Exception('Não foi possível obter manga_data')


# colocar properties "relationships" e "attributes" para facilitar?
class Manga:
    BASE_URL = 'https://api.mangadex.org'
    BASE_UPLOADS_URL = 'https://uploads.mangadex.org'

    def __init__(self, id:str):
        self.id = id
        self._init_properties()

    def _init_properties(self):
        'Função para organizar a inicialização das properties, definindo todas as variáveis necessárias como None, evitando a poluição do init'
        self._manga_data = {}

        self._title = ''
        self._genres = []
        self._content_rating = ''
        self._translated_languages = []

        self._cover_id = ''
        self._cover_filename = ''
        self._cover_image = None

        self._chapters_data = {}    
    @property
    def manga_data(self) -> dict:
        if not self._manga_data:
            try:
                response = requests.get(f'{self.BASE_URL}/manga/{self.id}')
                self._manga_data = response.json()['data']
            except Exception as e:
                print(f'Erro ao buscar os dados do mangá: {e}')
        return self._manga_data
    @manga_data.setter
    def manga_data(self, data:dict):
        self._manga_data = data
    
    @property
    def title(self) -> str:
        if not self._title:
            try:
                if not self.manga_data:
                    raise Exception('Não foi possível obter manga_data')
                self._title = self.manga_data['attributes']['title']['en']
            except Exception as e:
                print(f'Erro ao obter título do mangá: {e}')
        return self._title

    @property
    def content_rating(self) -> str: # "safe" | "suggestive" | "erotica" | "pornographic"
        # filtrar para remover erotica e pornographic?
        if not self._content_rating:
            try:
                if not self.manga_data:
                    raise Exception('Não foi possível obter manga_data')
                self._content_rating = self.manga_data['attributes']['contentRating']
            except Exception as e:
                print(f'Erro ao obter a classificação do conteúdo: {e}')
        
        return self._content_rating

    @property
    def genres(self) -> list[str]:
        if not self._genres:
            try:
                if not self.manga_data:
                    raise Exception('Não foi possível obter manga_data')
                tags = self.manga_data['attributes']['tags']
                for tag in tags:
                    if tag['attributes']['group'] == 'genre':
                        self._genres.append(tag['attributes']['name']['en'])
                        # retorna apenas os generos em ingles, mudar isso depois?
            except Exception as e:
                print(f'Erro ao obter os gêneros do mangá: {e}')
        return self._genres

    @property
    def translated_languages(self) -> list[str]:
        if not self._translated_languages:
            try:
                if not self.manga_data:
                    raise Exception('Não foi possível obter manga_data')
                self._translated_languages = self.manga_data['attributes']['availableTranslatedLanguages']
            except Exception as e:
                print(f'Erro ao obter os idiomas disponíveis: {e}')
        return self._translated_languages

    @property
    def cover_id(self) -> str:
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
    def cover_filename(self) -> str:
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
    def cover_image(self) -> Union[requests.Response, None]:
        if not self._cover_image:
            try:
                if not self.cover_filename:
                    raise Exception('Não foi possível obter o cover_filename')
                response = requests.get(f'{self.BASE_UPLOADS_URL}/covers/{self.id}/{self.cover_filename}')
                self._cover_image = response
                # self._cover_image = response.content
            except Exception as e:
                print(f'Erro ao buscar a imagem da cover_art: {e}')
        return self._cover_image 
    
    def get_chapters_data(self, language:str = 'pt-br') -> dict:
        if not self._chapters_data.get(language):
            try:
                url = f'{self.BASE_URL}/manga/{self.id}/feed/?translatedLanguage[]={language}'
                response = requests.get(url)
                
                self._chapters_data[language] = response.json()['data']
            except Exception as e:
                print(f'Erro ao obter os dados dos capítulos: {e}')
        
        # import json
        # with open('./app/api/chapters_data.json', 'w') as fw:
        #     json.dump(self._chapters_data, fw, indent=4)
        
        return self._chapters_data
    
    def get_chapter_data(self, chapter_number:Union[int, str], language:str = 'pt-br') -> dict:
        # chapter_data = {}
        try:
            for chapter in self.get_chapters_data(language)[language]:
                if chapter['attributes']['chapter'] == str(chapter_number):
                    chapter_data = chapter
                    chapter_data['id'] # só pra garantir que os dados que vieram estão certos
        except Exception as e:
            print(f'Erro ao obter os dados do capítulo {chapter_number}: {e}')
        return chapter_data
    
    def get_chapter_athome_data(self, chapter_number:Union[int,str], language:str = 'pt-br') -> dict:
        '''
        Parâmetros:
            - chapter_number: número do capítulo que os dados serão pegos
            - language: idioma do capítulo

        Retorna: um dicionário com os dados utilizados na busca das imagens dos capítulos
            - baseUrl -> str: a url onde será feita a busca das imagens
            - hash -> str: id para a busca das imagens do capítulo específico
            - data -> list[str]: lista com os nomes dos arquivos das imagens (filename)
            - dataSaver -> list[str]: lista com os nomes dos arquivos das imagens (filename), esses tem menos qualidade, logo são mais leves

        Como obter esses dados?
        ```python
            var = get_chapter_athome_data(chapter_number=1, language='en')

            urlBase = var['baseUrl']
            hash = var['chapter']['hash'] 
            data = var['chapter']['data']
            dataSaver = var['chapter']['dataSaver']
        ```
            
        Agora podemos fazer a requisição de uma imagem com:
            - urlBase/{hash}/{filename}
        '''
        athome_data = {}
        try:
            chapter = self.get_chapter_data(chapter_number, language)
            url = f'{self.BASE_URL}/at-home/server/{chapter['id']}'
            
            response = requests.get(url)        
            athome_data = response.json()
            # print(athome_data)
        except Exception as e:
            print(f'Erro ao obter os dados athome do capítulo: {e}')
        return athome_data
    
if __name__ == '__main__':
    jojo = Manga('1044287a-73df-48d0-b0b2-5327f32dd651')
    print(jojo.title)
    print(jojo.get_chapter_athome_data(1))