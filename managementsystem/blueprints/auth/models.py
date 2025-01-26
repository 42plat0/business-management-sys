from sqlalchemy import func
from sqlalchemy import event

from sqlalchemy import event
from flask_login import UserMixin

from managementsystem.app import db, login_manager
from managementsystem.helpers.hash.hash import get_salt, hash_password


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    username = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String, nullable=False)

    salt = db.Column(db.String, default=get_salt())

    created_at = db.Column(
        db.DateTime(timezone=True), default=func.localtimestamp()  # Current local time
    )

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


@event.listens_for(User.password, "set", retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        target.salt = get_salt()
        return hash_password(value, target.salt)

    return value
