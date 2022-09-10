# routes for app
from flask_app import app

from flask import render_template

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route("/about")
def about():
    # return html about page
    return "<h1>About Page</h1>"
