# ajuda
https://medium.com/@farhanahmedindia/complete-guide-deploying-a-flask-app-on-apache-ubuntu-c2f5d7b17e20

# instalar
sudo apt-get install libapache2-mod-wsgi-py3

# manga-and-chips.conf

<VirtualHost *:80>
    ServerName manga-and-chips.com
    ServerAdmin azevedodvictor@gmail.com
    WSGIDaemonProcess manga_and_chips home=/var/www/manga-and-chips python-home=/var/www/manga-and-chips/venv python-path=/var/www/manga-and-chips
    WSGIProcessGroup manga_and_chips
    WSGIScriptAlias / /var/www/manga-and-chips/wsgi.py
    <Directory /var/www/manga-and-chips>
        Require all granted
    </Directory>
    Alias /static /var/www/manga-and-chips/app/static
    <Directory /var/www/manga-and-chips/app/static>
        Require all granted
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/manga_and_chips_error.log
    CustomLog ${APACHE_LOG_DIR}/manga_and_chips_access.log combined
</VirtualHost>

# comandos de permissão

sudo chown -R flaskapp:www-data /home/flaskapp/myflaskapp
sudo chmod -R 755 /home/flaskapp/myflaskapp
sudo chmod 755 /home/flaskapp

# wsgi.py

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from app import app as application