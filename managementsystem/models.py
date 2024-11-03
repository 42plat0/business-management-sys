from managementsystem import db

from datetime import datetime

class User(db.Model):
    __tablename__= "Users"
    
    uid = db.Column(
        db.Integer, 
        primary_key=True,
        nullable=False
        )
    username = db.Column(
        db.String, 
        unique=True,
        nullable=False
        )
    
    password = db.Column(
        db.String, 
        unique=True,
        nullable=False
        )
    
    created_at = db.Column(
        db.DateTime,
        insert_default= datetime.now()
    )