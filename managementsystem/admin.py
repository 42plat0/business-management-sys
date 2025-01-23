import flask_login
from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView

from .blueprints.auth.models import User

def create_admin(app, db):
    admin = Admin(app, index_view=CafeAdminIndexView(), name="Pavadinimas")
    admin.add_view(UserView(User, db.session, name="Vartotojai"))
    admin.add_view(LogoutView(name="Atsijungti", endpoint="logout"))

class LogoutView(BaseView):
    @expose("/")
    def index(self):
        flask_login.logout_user()
        return redirect(url_for('auth.index'))

class UserView(ModelView):
    column_exclude_list = ['password', 'salt'] 

class CafeAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not flask_login.current_user.is_authenticated:
            return redirect(url_for('auth.login'))

        print(flask_login.current_user) 
        return super().index()