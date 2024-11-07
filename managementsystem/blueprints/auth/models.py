from sqlalchemy import func
from flask_login import UserMixin

from managementsystem.app import db, login_manager
from managementsystem.helpers.hash.hash import get_salt, hash_password, check_password

class User(db.Model, UserMixin):
    __tablename__= "users"
    
    uid = db.Column(
        db.Integer, 
        primary_key=True,
        nullable=False
        )
    
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    username = db.Column(
        db.String(20), 
        unique=True,
        nullable=False
        )
    
    password = db.Column(
        db.String, 
        nullable=False
        )
    
    salt = db.Column(
        db.String
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        default = func.localtimestamp() # Current local time
    )

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def get_salt(self):
        return get_salt()
    
    def generate_pw(self, password, salt):
        return hash_password(password, salt)

    def check_pw(self, password, hashed_pw):
        return check_password(password, hashed_pw)
