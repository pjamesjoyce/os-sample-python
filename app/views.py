from app import application
from flask import render_template


@application.route("/hello")
def hello():
    return "Hello"


@application.route("/template")
def template():
    return render_template('index.html')
