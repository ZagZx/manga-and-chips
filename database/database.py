import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from .query import insert, select
from typing import Union, Any

class Database:
    def __init__(self, db_path:str) -> None:
        '''
        Parâmetros:
            - db_path: Caminho e nome do arquivo onde o banco ficará armazenado
        '''
        self.db_path = db_path
        self._connection = None

    @property
    def connection(self) -> sqlite3.Connection:
        if not self._connection or not self.is_open():
            try: 
                self._connection = sqlite3.connect(self.db_path)
            except Exception as e:
                print(e)
        return self._connection
    
    def is_open(self) -> bool: 
        '''Checa se a conexão está aberta'''
        try: # roda um comando e se ele funcionar, a conexão está aberta
            self._connection.execute('SELECT 1')
            return True
        except: # se der erro, está fechada
            return False


    # AJUSTAR RUN QUERY PRA SER UTILIZADO DENTRO DA CLASSE EM FUNÇÕES COMO add_user
    def run_query(self, sql_query:str, params:Union[tuple[str], str] = None) -> list: # fazer doc depois
        result = None
        try:
            if params:
                cursor = self.connection.execute(sql_query, params)
            else:
                cursor = self.connection.execute(sql_query)

            self.connection.commit()
            result = cursor.fetchall()
        except Exception as e: # tirar quando entrar em produção
            print(e)
        self.connection.close()
        return result

    def run_sql_file(self, sql_path:str): # fazer doc
        with open(sql_path) as fr:
            self.connection.executescript(fr.read())
            self.connection.close()

    def add_user(self, username: str, email: str, password: str):
        '''
        Adiciona os dados do usuário na tabela users, criptografando a senha
        
        Parâmetros:
            - username: Nome do usuário
            - email: E-mail do usuário
            - password: Senha do usuário NÃO CRIPTOGRAFADA
        '''
        password_hash = generate_password_hash(password)
        query = insert('users', ('username', 'email', 'password_hash'))

        self.run_query(query, (username, email, password_hash))

if __name__ == '__main__':
    db = Database('./database/database.db')

    db.run_query("DELETE FROM sqlite_sequence WHERE name='users'") # tira os ids no autoincrement, só pra deixar bonito no sqlite viewer
    db.run_query("DELETE FROM users")
    db.add_user('ZagZ', 'azevedodvictor@gmail.com', 'senhaBEMdificil')

    print(db.run_query('SELECT * FROM users'))

    # print(db.run_query(select('users', 'id')))