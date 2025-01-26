import flask_login
from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView

from .blueprints.auth.models import User


class CafeAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        # Prevents from logging in not authenticated users
        if not flask_login.current_user.is_authenticated:
            return redirect(url_for('auth.login'))

        return super().index() # Returns admin page

class LogoutView(BaseView):
    @expose("/")
    def index(self):
        flask_login.logout_user()
        return redirect(url_for('auth.index'))

class UserView(ModelView):
    # Without seperate endpoint page
    create_modal = True
    edit_modal = True

    # View
    column_exclude_list = ['password', 'salt'] 

    # Edit/Create
    form_excluded_columns = ['salt', 'created_at']




def create_admin(app, db):
    admin = Admin(app, index_view=CafeAdminIndexView(), name="Pavadinimas")
    admin.add_view(UserView(User, db.session, name="Vartotojai"))
    admin.add_view(LogoutView(name="Atsijungti", endpoint="logout"))