import sqlite3

class Database:
    def __init__(self, db_path:str) -> None:
        '''
        Parâmetros:
            - sql_path: Caminho do SQL principal, que contém a criação de todas as tabelas
            - db_path: Caminho e nome do arquivo onde o banco ficará armazenado
        '''
        self.db_path = db_path
        self._connection = None

    @property
    def connection(self) -> sqlite3.Connection:
        if self._connection or not self.is_open():
            self._connection = sqlite3.connect(self.db_path)
        return self._connection
    
    def is_open(self) -> bool:
        '''Checa se a conexão está aberta'''
        try: # roda um comando e se ele funcionar, a conexão está aberta
            self._connection.execute('SELECT 1;')
            return True
        except: # se der erro, está fechada
            return False

    def run_sql_file(self, sql_path:str):
        with open(sql_path) as fr:
            self.connection.executescript(fr.read())
            self.connection.close()

if __name__ == '__main__':
    db = Database('./database/schema.sql', './database/database.db')