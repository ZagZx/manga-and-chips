from flask_login import UserMixin
from typing import Union

class User(UserMixin):
    def __init__(self, id:Union[int, str],username:str, email:str) -> None:
        self.id = id
        self.username = username
        self.email = email
