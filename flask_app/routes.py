# routes for app
from flask_app import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/about")
def about():
    # return html about page
    return "<h1>About Page</h1>"
