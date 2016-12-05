# __init__.py -- app
from flask import Flask

app = Flask(__name__)
# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = None

from .resources import *

@app.route("/")
def index():
    return "IOTAP REST API"
