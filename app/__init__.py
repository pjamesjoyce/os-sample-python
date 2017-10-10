from flask import Flask  
#from .views import *

application = Flask(__name__)
application.config.from_pyfile('app.cfg')

def uc_first(string):
    return string[0].upper() + string[1:]


application.jinja_env.filters['uc_first'] = uc_first  


@application.route("/test")
def hello():
    return "<h1>Hello from the World of __init__.py again!</h1> <p>{}</p>".format(application.config['SQLALCHEMY_DATABASE_URI'])

message = "James says hello, also {}".format(application.config['SQLALCHEMY_DATABASE_URI'])
