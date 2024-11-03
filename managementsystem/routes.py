from flask import render_template, request
from managementsystem import app
from managementsystem.forms import RegisterForm, LoginForm

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template(
        "home.html"
    )



@app.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()

    # POST req and VALID form
    if form.validate_on_submit():
        pass

    return render_template(
        "login.html",
        title="Login",
        form=form
    )

@app.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()

    # POST req and VALID form
    if form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]
        c_password = request.form["confirm_password"]
       
    return render_template(
        "register.html",
        title="Register",
        form=form
    )