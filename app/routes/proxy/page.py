from flask import request, Response
import requests
from time import time

from . import proxy_bp


@proxy_bp.route('/page/<hash>/<filename>')
def page(hash:str, filename:str):
    base_url = request.args.get('baseUrl') # url otimizada para buscar as imagens
    
    if not base_url:
        base_url = 'https://uploads.mangadex.org'
    
    url = f'{base_url}/data/{hash}/{filename}'
   
    before = time()
    response = requests.get(url)
    now = time()

    print('\n====PAGE PROXY====')
    print('url:',url)
    print(f'Tempo de Execução: {round(now-before,2)}s\n')

    if response.status_code == 200:
        return Response(response.content, content_type=response.headers['Content-Type'])
    else:
        return Response('Not found', response.status_code)

