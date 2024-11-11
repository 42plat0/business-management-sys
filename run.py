from managementsystem.app import create_app

f_app = create_app()

if __name__ == "__main__":
    
    f_app.run(debug=True)