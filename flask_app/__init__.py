from flask import Flask
# from flask_wtf.csrf import CSRFProtect
# import os

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.urandom(24)
# csrf = CSRFProtect(app)

from flask_app import routes
from flask_app import admin_routes
