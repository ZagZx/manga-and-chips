from flask_login import UserMixin
from typing import Union

class User(UserMixin):
    def __init__(self, id:Union[int, str],username:str, email:str, password_hash:str) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash