from managementsystem import app, db

if __name__ == "__main__":
    # Create database
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)