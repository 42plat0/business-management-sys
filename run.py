from managementsystem.app import create_app

f_app = create_app()

if __name__ == "__main__":

    # with app.app_context():
    #     db.create_all()
    
    f_app.run(debug=True)