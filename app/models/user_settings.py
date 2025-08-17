from sqlalchemy import Column, Integer, ForeignKey, Boolean
from app import db

class UserSettings(db.Model):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # mudar isso depois pra ter uma tabela associativa só para os tipos de conteudos do usuário
    safe = Column(Boolean, default=True, nullable=False)
    suggestive = Column(Boolean, default=True, nullable=False)
    erotica = Column(Boolean, default=False, nullable=False)
    pornographic = Column(Boolean, default=False, nullable=False)
    