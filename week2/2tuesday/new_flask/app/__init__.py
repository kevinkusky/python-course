from flask import Flask
from app.config import Config

app = Flask(__name__)

from app import routes  # noqa


app.config.from_object(Config)
# print(app.config['SECRET_KEY'])

