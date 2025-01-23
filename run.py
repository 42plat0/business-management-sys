from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from managementsystem.app import create_app, db
from managementsystem.blueprints.auth.models import User

f_app = create_app()

if __name__ == "__main__":

    admin = Admin(f_app, name="cafe")
    admin.add_view(ModelView(User, db.session))

    f_app.run(debug=True)