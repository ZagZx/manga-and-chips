import os
from secrets import token_hex
import subprocess
import sys

def beauty_print(string:str):
    print('='*45)
    print(string)
    print('='*45)

STEPS = 3

print('Iniciando Build')

dotenv_path = './.env'
if not os.path.exists(dotenv_path):
    secret_key = token_hex()
    database_url = "sqlite:///database.db"

    with open(dotenv_path, 'w') as fw:
        fw.write(f'SECRET_KEY="{secret_key}"\n')
        fw.write(f'DATABASE_URL="{database_url}"')
    beauty_print(f'Arquivo .env criado | 1/{STEPS}')
else:
    beauty_print(f'Arquivo .env já existe | 1/{STEPS}')


venv_path = './venv'
if not os.path.exists(venv_path):
    subprocess.run([sys.executable, '-m', 'venv', venv_path], check=True)
    beauty_print(f'Ambiente virtual criado | 2/{STEPS}')
else:
    beauty_print(f'Ambiente virtual já existe | 2/{STEPS}')


pip_bin = ''
if os.name == 'posix':  # Unix (Linux, macOS)
    pip_bin = os.path.join(venv_path, 'bin', 'pip')
elif os.name == 'nt':
    pip_bin = os.path.join(venv_path, 'Scripts', 'pip.exe')
requirements_file = 'requirements.txt'
subprocess.run([pip_bin, 'install', '-r', requirements_file], check=True)
beauty_print(f'Dependências instaladas | 3/{STEPS}')
