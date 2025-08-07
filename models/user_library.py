from sqlalchemy import Column, String, Integer, ForeignKey
from models import db

class UserLibrary(db.Model):
    __tablename__ = "user_library"

    id = Column(Integer, primary_key=True, autoincrement=True)
    manga_id = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    