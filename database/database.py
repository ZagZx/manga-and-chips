import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as fr:
    connection.executescript(fr.read())

connection.close()


class Database:
    def __init__(self) -> None:
        pass