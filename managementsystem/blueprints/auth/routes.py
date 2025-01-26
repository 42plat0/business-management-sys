from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_user, login_required, logout_user, current_user

from managementsystem.app import db
from managementsystem.blueprints.auth.forms import RegisterForm, LoginForm
from managementsystem.blueprints.auth.models import User

from managementsystem.helpers.hash.hash import get_salt, hash_password, check_password

auth = Blueprint("auth", __name__, template_folder="./templates", static_folder="static")


@auth.route("/")
def index():
    return render_template("index.html")


@auth.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()

    # POST req and VALID form
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user:
            # Check if password is valid
            entered_hashed_password = hash_password(password, user.salt)

            valid_password = check_password(entered_hashed_password, user.password)

            if not valid_password:
                flash("Password is incorrect!")
                return redirect(url_for("auth.login"))

            login_user(user)
            return redirect(url_for("home.index"))

        flash("User with specified username doesn't exist.")
        return redirect(url_for("auth.login"))

    return render_template("login.html", title="Login", form=form)


@auth.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()

    # POST req and VALID form
    if form.validate_on_submit():
        # Get data from form
        username = form.username.data
        email = form.email.data
        password = form.password.data

        username_exists = User.query.filter_by(username=username).first()
        email_exists = User.query.filter_by(email=email).first()

        if not username_exists and not email_exists:
            new_user = User(username=username, email=email, password=password)

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for("home.index"))

        elif username_exists:
            flash("Username is taken.")
        else:
            flash("Email is taken.")

    return render_template("register.html", title="Register", form=form)


@auth.route("/logoff", methods=("GET", "POST"))
def logoff():
    logout_user()
    return redirect(url_for("auth.index"))


import json


@auth.route("/api/hey", methods=("GET",))
def hey():
    return json.dumps({"id": 2, "days": [1, 2, 3, 4, 5, 6, 7]})
    pass
