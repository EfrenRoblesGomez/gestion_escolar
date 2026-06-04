import os
from dotenv import load_dotenv

load_dotenv()

class Configuracion:
    SECRET_KEY = os.environ.get('SECRET_KEY', '1234')

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://avnadmin:AVNS_WE9_KEHQsbc15PD5FHE@mysql-f382ebf-cbtis.b.aivencloud.com:26910/defaultdb'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
