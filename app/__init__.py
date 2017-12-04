from flask import flask
#initialize application
app = Flask(__name__)

from app import views
#allows for views creation
