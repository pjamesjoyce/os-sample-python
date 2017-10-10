from app import application
from flask import render_template, request, redirect


@application.route("/hello")
def hello_view():
    return "Hello"


@application.route("/")
def template():
    current_user = {'is_authenticated': True, 'name':'James'}
    return render_template('index.html', current_user=current_user)

