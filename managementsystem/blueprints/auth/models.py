from managementsystem.app import db

from sqlalchemy import func

class User(db.Model):
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

    created_at = db.Column(
        db.DateTime(timezone=True),
        default = func.localtimestamp() # Current local time
    )
