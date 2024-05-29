from dotenv import load_dotenv
from os import getenv

from pathlib import Path

dotenv_path = Path('../.env')

load_dotenv()

SQLALCHEMY_DATABASE_URI = getenv("FLASK_SQLALCHEMY_DATABASE_URI", "12212121212")
SQLALCHEMY_TRACK_MODIFICATIONS = getenv("FLASK_SQLALCHEMY_DATABASE_URI", False)
SECRET_KEY = getenv("FLASK_SECRET_KEY", False)
SQLALCHEMY_ECHO = getenv("FLASK_SQLALCHEMY_ECHO", True)