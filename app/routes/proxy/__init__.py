from flask import Blueprint

proxy_bp = Blueprint('proxy',__name__, url_prefix='/proxy')

from . import cover