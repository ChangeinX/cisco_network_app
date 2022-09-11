from flask_app import app
from flask import render_template, url_for, redirect, request
from database import device_db_handler
import pandas as pd
import plotly
import plotly.express as px


@app.route('/admin/dashboard/<username>')
def admin_dashboard(username):
    # use pandas to make a table of the devices
    df = pd.DataFrame(device_db_handler.get_devices())
    # render the template
    return render_template('admin/templates/dashboard.html', username=username,
                           tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route("/profile/<username>")
def admin_profile(username):
    print(f'Admin Profile for {username}')
    return f"Admin Profile for {username}"
