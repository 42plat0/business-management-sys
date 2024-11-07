from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_user, login_required, logout_user, current_user

from managementsystem.app import db
from managementsystem.blueprints.auth.forms import RegisterForm, LoginForm
from managementsystem.blueprints.auth.models import User

from managementsystem.helpers.hash.hash import get_salt, hash_password, check_password

auth = Blueprint("auth", __name__, template_folder="templates")

@auth.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()

    # POST req and VALID form
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if not user:
            return redirect(url_for("home.index"))

        return "Success!"


    return render_template(
        "login.html",
        title="Login",
        form=form
    )

@auth.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()

    # POST req and VALID form
    if form.validate_on_submit():
        # Get data from form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()

        if not user:
            salt = get_salt()
            password_hash = hash_password(password, salt)

            new_user = User(username=username, email=email, password=password_hash, salt=salt)
        
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("home.index"))

        flash("Username is taken. Choose another one.")
       
    return render_template(
        "register.html",
        title="Register",
        form=form
    )