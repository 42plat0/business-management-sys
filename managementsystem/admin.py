from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .blueprints.auth.models import User

def create_admin(app, db):
    admin = Admin(app, name="cafe")
    admin.add_view(ModelView(User, db.session))