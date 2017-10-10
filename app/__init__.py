from flask import Flask  
#from .views import *

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello from the World of __init__.py again!"

message = "James says hello"
