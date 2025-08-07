from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, DeclarativeBase

Base:DeclarativeBase = declarative_base()

engine = create_engine("sqlite:///bancofalso.db")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)


class UserLibrary(Base):
    __tablename__ = "user_library"

    id = Column(Integer, primary_key=True, autoincrement=True)
    manga_id = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


# CREATE TABLE IF NOT EXISTS user_library(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     manga_id TEXT NOT NULL, -- VARCHAR(255) em MySQL
#     -- last_read_chapter INTEGER,
#     user_id INTEGER NOT NULL,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );

if __name__ == "__main__":
    Base.metadata.create_all(engine)
