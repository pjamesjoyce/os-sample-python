from flask import Flask  


application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello from the World of __init__.py!"

message = "James says hello"
