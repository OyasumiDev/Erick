import os
from dotenv import load_dotenv
from config.eliminar_cache import eliminar_pycache

# Cargar el entorno
load_dotenv()

# Eliminar __pycache__ al inicio
eliminar_pycache()

# Cargar las credenciales de la base de datos
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')
DB_TYPE = os.environ.get('DB_TYPE')
