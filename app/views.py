from app import application
from flask import render_template


@application.route("/hello")
def hello_view():
    return "Hello"


@application.route("/template")
def template():
    args = {}
    current_user = {'is_authenticated': True, 'name':'James'}
    return render_template('index.html', current_user=current_user)
