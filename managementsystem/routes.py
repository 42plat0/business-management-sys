from flask import render_template, request
from managementsystem import app

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template(
        "home.html"
    )



@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

    return render_template(
        "login.html",
        title="Title",
        content="Content"
    )

@app.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conf_password = request.form["conf_password"]

       
    return render_template(
        "register.html",
        content="Content"
    )