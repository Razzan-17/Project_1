import os

from dotenv import load_dotenv

load_dotenv()

login = os.getenv('login_DB')
password = os.getenv('password_DB')
name_DB = os.getenv('name_DB')

SECRET = os.getenv('SECRET')
URI = f'postgresql://{login}:{password}@localhost/{name_DB}'
URI_test = f'postgresql://{login}:{password}@localhost/test_Flask'
