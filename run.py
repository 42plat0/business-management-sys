from managementsystem.app import create_app, db
from managementsystem.admin import create_admin

f_app = create_app()

if __name__ == "__main__":
    create_admin(f_app, db)

    f_app.run(debug=True)