from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Integer, String, DateTime

app = Flask(__name__)

app.config.from_pyfile("config.py", silent=True)

db = SQLAlchemy(app)

from managementsystem import routes