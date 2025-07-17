-- convenção utilizada: tabelas e colunas em inglês e no plural

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- AUTO_INCREMENT em MySQL
    username TEXT NOT NULL, -- VARCHAR(255) em MySQL
    email TEXT NOT NULL UNIQUE, -- VARCHAR(255) em MySQL
    password_hash TEXT NOT NULL -- VARCHAR(255) em MySQL
); 