from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Secret key, database uri
app.config.from_pyfile("config.py", silent=True)

db = SQLAlchemy(app)

from managementsystem import routes