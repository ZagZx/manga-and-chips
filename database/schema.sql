-- convenção utilizada: tabelas e colunas em inglês e no plural

DROP TABLE IF EXISTS users; -- tirar depois

CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- AUTO_INCREMENT em MySQL
    username TEXT NOT NULL, -- VARCHAR(255) em MySQL
    email TEXT NOT NULL UNIQUE, -- VARCHAR(255) em MySQL
    password_hash TEXT NOT NULL -- VARCHAR(255) em MySQL
); 

DROP TABLE IF EXISTS user_library; -- tirar depois

CREATE TABLE IF NOT EXISTS library(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manga_id TEXT NOT NULL, -- VARCHAR(255) em MySQL
    -- last_read_chapter INTEGER,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) 
);