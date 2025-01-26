from flask import render_template, Blueprint
from flask_login import login_required

home = Blueprint("home", __name__, template_folder="templates")


@home.route("/")
@home.route("/home")
@home.route("/index")
@login_required
def index():
    return render_template("home.html")
