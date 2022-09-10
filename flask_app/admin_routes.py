# routes for app
from flask_app import app

@app.route('/admin/dashboard')
def admin_dashboard():
    return "Admin Dashboard"

@app.route("/about")
def aadmin_profile():
    # return html about page
    return "Admin Profile"
