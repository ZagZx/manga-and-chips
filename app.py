from flask import Flask
from flask_login import LoginManager

from dotenv import load_dotenv
import os

from models import db, User, UserLibrary

from routes.auth import auth_bp
from routes.manga import manga_bp
from routes.proxy import proxy_bp
from routes.index import index_bp
from routes.search import search_bp

load_dotenv('./.env')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
with app.app_context():
    db.create_all()

    # from werkzeug.security import generate_password_hash
    # db.session.add(User(username='ZagZ', email='zezi@example.com', password_hash=generate_password_hash('123')))
    # db.session.commit()

    # user:User = User.query.get(1)
    # print('\n',user.id, user.username, user.email, '\n')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.register_blueprint(auth_bp)
app.register_blueprint(manga_bp)
app.register_blueprint(proxy_bp)
app.register_blueprint(index_bp)
app.register_blueprint(search_bp)






































# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/search')
# def search():
#     title = request.args.get('query')
#     results = search_manga_by_title(title)

#     mangas_list = []
#     for manga_data in results:
#         manga = Manga(manga_data['id'])
#         manga.manga_data = manga_data

#         mangas_list.append(
#             {
#                 "id": manga.id,
#                 "title": manga.title,
#                 "cover_image": url_for('cover_proxy_by_manga_id', manga_id = manga.id)
#             }
#         )

#     return render_template('search.html', mangas_list = mangas_list)

# @app.route('/cadastro', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password_hash = generate_password_hash(request.form.get('password'))

#         if not db.run_query(f"SELECT * FROM users WHERE email = ?", email):
#             db.run_query(f"INSERT INTO users(username, email, password_hash) VALUES (?, ?, ?)", (username, email, password_hash))
#             return redirect(url_for('login'))
#         else: 
#             print('Já existe um usuário cadastrado com esse email')
#             return render_template('register.html') # colocar mensagem de erro
#     if request.method == 'GET':
#         return render_template('register.html')

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     # fazer tratamento de erros caso a senha esteja errada
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user_data = db.run_query('SELECT id, username, password_hash FROM users WHERE email = ?', (email,))
#         if user_data:
#             user_data = user_data[0]
#             if check_password_hash(user_data[2], password):
#                 user = User(id=user_data[0], username=user_data[1], email=email)
#                 login_user(user)
#                 return redirect(url_for('index'))
#             else:
#                 print('Senha errada')
#         # else:
#         #     print('Email não cadastrado')
#         return render_template('login.html') # colocar mensagem de erro
#     elif request.method == 'GET':
#         return render_template('login.html')

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()

#     return redirect(url_for('index'))

# # @app.route("/manga/<manga_id>/chapter/<chapter_number>")
# # def read_chapter(manga_id:str, chapter_number:str):
# #     manga = Manga(manga_id)
# #     chapter = manga.get_chapter_athome_data(chapter_number, 'pt-br')
    
# #     # print(chapter)
# #     baseUrl = chapter['baseUrl']
# #     filename = chapter['chapter']['data'][int(chapter_number)]
# #     hash = chapter['chapter']['hash']
# #     print(url_for('chapter_proxy', baseUrl=baseUrl, hash=hash, filename=filename, chapter_number=1))
    
# #     return render_template('chapter.html', chapter=chapter)

# # @app.route('/chapter-proxy/<baseUrl>/<hash>/<filename>/<chapter_number>')
# # def chapter_proxy():
    
# #     return Response()

# @app.route('/cover-proxy/<manga_id>/<filename>')
# def cover_proxy(manga_id:str, filename:str):
#     before = time.time()
    
#     manga = Manga(manga_id)

#     if filename and manga_id:
#         cover_image = manga.cover_image

#         now = time.time()
#         print('\n====COVER PROXY====')
#         print(f'Mangá: {manga.title}')
#         print(f'Tempo de Execução: {round(now-before,2)}s\n')

#         return Response(cover_image.content, content_type=cover_image.headers['Content-Type'])
    
# @app.route('/cover_proxy/<manga_id>')
# def cover_proxy_by_manga_id(manga_id):
#     '''
#     Gambiarra para acelerar a pesquisa, ao invés de passar os filenames e travar a página por muito tempo,
#     é passado no dicionário um url_for para esta rota e nela é obtido o filename e então ela redireciona para a cover_proxy.

#     Ou seja, aumenta o tempo de carregamento das imagens para diminuir consideravelmente o tempo de tela travada.
#     '''

#     manga = Manga(manga_id)
#     cover_filename = manga.cover_filename
#     return redirect(url_for('cover_proxy', manga_id = manga_id, filename = cover_filename))