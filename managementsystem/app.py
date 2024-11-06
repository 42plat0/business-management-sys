from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config["SECRET_KEY"] = "1901569539ec311888b9d108"
    
    db.init_app(app)
    login_manager.init_app(app)

    # Add blueprints
    from managementsystem.blueprints.home.routes import home as home_bp
    from managementsystem.blueprints.auth.routes import auth as auth_bp

    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    migrate = Migrate(app, db)
    
    return app