from flask import render_template
from flask_paginate import Pagination, get_page_args

from database import device_db_handler
from database import user_pass
from flask_app import app


@app.route('/admin/dashboard/<username>')
def admin_dashboard(username):
    # build table of devices from database and paginate
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    # set default page size
    per_page = 25
    total = len(device_db_handler.get_device_info())
    pagination_devices = device_db_handler.get_device_info()[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    # only show if user is authenticated
    if user_pass.check_admin(username):
        return render_template('admin/templates/dashboard.html', username=username, devices=pagination_devices, page=page,
                               per_page=per_page, pagination=pagination)


# dynamic route to click on a device and load its information
@app.route('/admin/device/<username>/<device_name>')
def admin_device(username, name):
    device = device_db_handler.get_device_by_name(name)
    return render_template('admin/templates/device.html', username=username, device=device)


@app.route("/profile/<username>")
def admin_profile(username):
    print(f'Admin Profile for {username}')
    return f"Admin Profile for {username}"
