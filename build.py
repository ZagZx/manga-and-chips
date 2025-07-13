import os
from secrets import token_hex

ENV_PATH = './.env'

if not os.path.exists(ENV_PATH):
    secret_key = token_hex()

    with open(ENV_PATH, 'w') as fw:
        fw.write(f'SECRET_KEY="{secret_key}"\n')
    print(f'Arquivo .env criado')
else:
    print(f'.env já existe. Nenhuma alteração feita')
