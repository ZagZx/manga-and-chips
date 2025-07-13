# Requisitos Funcionais 

### Tema

Site para ler mangás, podendo adiciona-los a uma biblioteca para acompanhar o mangá.

### Cadastro e autenticação

- RF01: Usuário poderá criar conta com e-mail, senha e nome de usuário.

- RF02: Usuário poderá fazer login/logout.

- RF03: Senhas com hash seguro.

### Gerenciamento do recurso

- RF04: Usuário poderá adicionar mangás a sua biblioteca. (CREATE)

- RF05: Usuário poderá ver os mangás da sua biblioteca. (READ)

- RF06: Usuário poderá editar seu nome de usuário. (UPDATE)

- RF07: Usuário poderá remover mangás da sua biblioteca. (DELETE)

### Pesquisa

- RF08: Possibilidade pesquisar os mangás por nome.

- RF09: Possibilidade de pesquisar os mangás por categoria, em uma página onde os mangás são ordenados por ordem alfabética e pode-se selecionar uma letra para exibir apenas os mangás que comecem com aquela letra. 

# Requisitos não funcionais

### Backend

- RNF01: Backend em Python utilizando o framework Flask.

- RNF02: Extensão flask-login para autenticação.

- RNF03: SQLite para o gerenciamento do banco de dados de usuários e dados do recurso.

- RNF04: API do MangaDex para download de páginas do mangá, pesquisa, capas, etc.

### Frontend

- RNF05: HTML, CSS e Javascript.

- RNF06: Framework Tailwind ou Boostrap para facilitar o desenvolvimento da interface.

### Banco de Dados

- RNF07: Linguagem MySQL.

### Templates

- RNF08: Uso de extends/includes para layout e mensagens de erro.

- RNF09: Páginas de erro personalizadas.

### Documentações e instruções

- RNF10: Código versionado no GitHub com entregas semanais.

- RNF11: Modelo conceitual e/ou lógico do banco de dados.

- RNF12: README com instruções.