import flask_login
from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView

from .blueprints.auth.models import User

def create_admin(app, db):
    admin = Admin(app, index_view=CafeAdminIndexView(), name="cafe")
    admin.add_view(CafeModelView(User, db.session))

class CafeModelView(ModelView):
    
    def is_accessible(self):
        return flask_login.current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('blueprints.auth.login'))

class CafeAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not flask_login.current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        
        return super().index()
  
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))