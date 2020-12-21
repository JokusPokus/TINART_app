from flask import render_template

from . import main


@main.route("/")
def index():
    return render_template("landing.html")


@main.route("/simulator")
def start_simulator():
    return render_template("app.html")
