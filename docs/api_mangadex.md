**JoJo parte 7:**
- **manga_id:** 1044287a-73df-48d0-b0b2-5327f32dd651
- **cover_id:** 6c0a3578-f000-4226-a592-bec6fae582f2
- **cover_jpg:** e7e5e267-502f-4b77-9f19-b7ea1344f68f.jpg

### Busca por título
Busca pelo título informações do mangá.
- **baseURL:** api.mangadex.org
- **endpoint:** /manga?title={titulo do mangá} 

**Retorna:** ID {manga_id}, capa {cover_id}, título completo, gêneros, classificação de **todos os mangás** que contenham o título pesquisado no nome

### Busca por ID
Busca pelo ID informações do mangá.
- **baseURL:** api.mangadex.org
- **endpoint:** /manga/{manga_id} 

**Retorna:** ID {manga_id}, capa {cover_id}, título completo, gêneros, classificação do **mangá específico**

### Cover Info
Busca informações do Cover.
- **baseURL:** api.mangadex.org
- **endpoint:** /cover/{cover_id}

**Retorna:** Nome do arquivo jpg da cover {cover_jpg}

### Cover Image
Exibe a imagem da capa.
- **baseURL:** uploads.mangadex.org
- **endpoint:** /covers/{manga_id}/{cover_jpg}

**Retorna:** Imagem da capa do mangá
