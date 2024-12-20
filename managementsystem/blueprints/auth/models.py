from sqlalchemy import func
from flask_login import UserMixin

from managementsystem.app import db, login_manager

class User(db.Model, UserMixin):
    __tablename__= "users"
    
    id = db.Column(
        db.Integer, 
        primary_key=True,
        nullable=False
        )

    username = db.Column(
        db.String(20), 
        unique=True,
        nullable=False
    )
    
    email = db.Column(
        db.String(120),
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
    def load_user(id):
        return User.query.get(int(id))
    
