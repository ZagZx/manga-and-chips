from flask import render_template, Blueprint
from app.api import get_last_uploaded_mangas

index_bp = Blueprint('index',__name__)

@index_bp.route('/')
def index():
    # last_uploaded = get_last_uploaded_mangas()
    return render_template('index.html')

