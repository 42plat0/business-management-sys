from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Integer, String, DateTime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

from managementsystem import routes