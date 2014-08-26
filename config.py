import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CSRF_ENABLED = True
DEBUG = False
BCRYPT_LOG_ROUNDS = 12

# From https://gist.github.com/ndarville/3452907
try:
    SECRET_KEY
except NameError:
    SECREY_KEY_FILE = os.path.join(PROJECT_DIR, 'secret.txt')
    try:
        SECRET_KEY = open(SECREY_KEY_FILE).read().strip()
    except IOError:
        SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

try:
    EMAIL_CONFIRM_SALT
except NameError:
    SECRET_SALT_FILE = os.path.join(PROJECT_DIR, 'salt.txt')
    try:
        EMAIL_CONFIRM_SALT = open(SECRET_SALT_FILE).read().strip()
    except IOError:
        EMAIL_CONFIRM_SALT = os.environ.get('FLASK_EMAIL_SALT')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PROJECT_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(PROJECT_DIR, 'db_repository')
