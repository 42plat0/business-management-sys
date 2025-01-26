from flask import render_template, Blueprint

schedule = Blueprint("schedule", __name__, template_folder="templates")


@schedule.route("/")
def index():
    return render_template("schedule.html")
