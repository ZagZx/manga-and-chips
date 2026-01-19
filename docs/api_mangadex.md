**JoJo parte 7:**
- **manga_id:** 1044287a-73df-48d0-b0b2-5327f32dd651
- **cover_id:** 6c0a3578-f000-4226-a592-bec6fae582f2
- **cover_jpg:** e7e5e267-502f-4b77-9f19-b7ea1344f68f.jpg
- **chapter_id:** 87ac4e0c-f931-4777-9d86-32f2f277c3cc

## Busca por título
Busca pelo título informações do mangá.
- **baseURL:** api.mangadex.org
- **endpoint:** /manga?title={titulo do mangá} 

**Retorna:** ID {manga_id}, capa {cover_id}, título completo, gêneros, classificação de **todos os mangás** que contenham o título pesquisado no nome

## Busca por ID
Busca pelo ID informações do mangá.
- **baseURL:** api.mangadex.org
- **endpoint:** /manga/{manga_id} 

**Retorna:** ID {manga_id}, capa {cover_id}, título completo, gêneros, classificação do **mangá específico**

## Cover Info
Busca informações do Cover.
- **baseURL:** api.mangadex.org
- **endpoint:** /cover/{cover_id}

**Retorna:** Nome do arquivo jpg da cover {cover_filename}

## Cover Image
Exibe a imagem da capa.
- **baseURL:** uploads.mangadex.org
- **endpoint:** /covers/{manga_id}/{cover_filename}

**Retorna:** Imagem da capa do mangá

## Todos os capítulos de um mangá
Busca os dados de todos os capítulos por idioma(s)
- **baseURL:** api.mangadex.org
- **endpoint:** /manga/{manga_id}/feed?translatedLanguage[]={idioma do mangá}
- **exemplo:** api.mangadex.org/manga/044287a-73df-48d0-b0b2-5327f32dd651/feed?translatedLanguage[]=pt-br

**Retorna:** Os dados de todos os capítulos
- ID
- Título
- Número do capítulo e volume
- Quantidade de páginas
- Relacionamentos (Mangá, scan que traduziu, usuário que deu upload)
 (id, numero do capitulo, qnt de paginas, relacionamentos)

## Buscar nome de arquivo das páginas do capítulo
Busca nomes dos arquivos das imagens de páginas do capítulo especificado por id
- **baseURL:** api.mangadex.org
- **endpoint:** /at-home/server/{chapter_id}

**Retorna:** Nomes dos arquivos das imagens (data ou dataSaver) de páginas do capítulo especificado
https://api.mangadex.org/at-home/server/1613cd84-53ea-4ad9-b09d-724d55c18ef4

## Imagem de página