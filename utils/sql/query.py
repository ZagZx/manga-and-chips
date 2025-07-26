'''
Funções que retornam uma string formatada com parâmetros para serem utilizados no SQLite

Isso vai mesmo ser utilizado??
'''

from typing import Union

def insert(table: str, rows: Union[tuple[str], list[str], str]) -> str:
    '''
    Formata uma string para um insert SQL com placeholders(?) equivalentes a quantidade de linhas

    Parâmetros:
        - table: Nome da tabela
        - rows: Tupla com o nome das linhas ("username", "email", "password_hash") ou caso seja uma única linha, apenas o nome da linha em string "username"

    Retorna:
        - Uma string de INSERT como essa: "INSERT INTO users(username, email, password_hash) VALUES (?, ?, ?)"
    '''
    placeholders = '?'
    if isinstance(rows, (list, tuple)):
        placeholders = ', '.join(['?'] * len(rows))
        rows = ', '.join(rows)
        
    return f'INSERT INTO {table}({rows}) VALUES ({placeholders})'

def select(table: str, rows: Union[tuple[str], list[str], str] = "*") -> str:
    '''
    Formata uma string para um SELECT SQL.

    Parâmetros:
        - table: Nome da tabela
        - rows: Tupla com os nomes das colunas ("id", "username"), caso não seja informado o parâmetro, o mesmo será "*", que selecionará todas as linhas de uma tabela

    Retorna:
        - Uma string de SELECT como esta: "SELECT id, username FROM users"
          ou, se o valor padrão for usado: "SELECT * FROM users"
    '''
    if isinstance(rows, (list, tuple)):
        rows = ', '.join(rows)
        
    return f'SELECT {rows} FROM {table}'

if __name__ == '__main__':
    print()
    print(insert('users', 'username'))
    print()
    print(insert('users', ['username', 'email', 'password_hash']))
    print()
    print(select('users'))
    print()
    print(select('users', ('id', 'username')))