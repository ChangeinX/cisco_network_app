from flask import render_template, redirect, url_for, request
from flask_paginate import Pagination, get_page_args

from database import device_db_handler
from database import user_pass
from flask_app import app


@app.route('/admin/dashboard/')
def admin_dashboard():
    # build table of devices from database and paginate
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    # set default page size
    per_page = 15
    total = len(device_db_handler.get_device_info())
    pagination_devices = device_db_handler.get_device_info()[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('admin/templates/dashboard.html',
                           devices=pagination_devices,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


# if button id="ping" is pressed ping the device and refresh the page
@app.route('/admin/dashboard/', methods=['POST'])
def ping_device():
    # ping the device if submit button was pressed in the table
    if request.method == 'POST':
        if request.form['dynamic_button']:
            # ping the device
            print(f'pinging {request.form["dynamic_button"]}')
            device_db_handler.get_device_status_by_ping(request.form['dynamic_button'])
            # refresh the page
            return redirect(url_for('admin_dashboard'))
    return redirect(url_for('admin_dashboard'))



# dynamic route to click on a device and load its information
@app.route('/admin/device/<device_name>', methods=['GET', 'POST'])
def admin_device(name):
    if request.method == 'POST':
        device = device_db_handler.get_device_by_name(name)
        return render_template('admin/templates/device.html', device=device)
    else:
        return redirect(url_for('admin_dashboard'))

@app.route("/profile/<username>")
def admin_profile(username):
    print(f'Admin Profile for {username}')
    return f"Admin Profile for {username}"

@app.route("/admin/config/device", methods=['GET', 'POST'])
def admin_config_device():
    return render_template('admin/templates/config_device.html')