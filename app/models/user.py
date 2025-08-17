from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    library = relationship("UserLibrary", cascade="all, delete")
    settings =  relationship("UserSettings", cascade="all, delete")