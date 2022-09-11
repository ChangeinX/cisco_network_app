from flask_app import app

from flask import render_template, url_for, redirect, request

from database import user_pass

# main page is a login page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the user exists
        if user_pass.check_user(request.form['username']):
            print(f'{request.form["username"]} exists')
            # check if the password is correct
            if user_pass.check_password(request.form['username'], request.form['password']):
                # check if the user is an admin
                if user_pass.check_admin(request.form['username']):
                    print(f'{request.form["username"]} is an admin')
                    return redirect(url_for('admin_dashboard', username=request.form['username']))
                else:
                    return redirect(url_for('index'))
            else:
                return "Incorrect Password"
        else:
            return "User does not exist"
    else:
        return render_template('public/templates/public_main.html')

@app.route("/about")
def about():
    # return html about page
    return "<h1>About Page</h1>"


# routes when register is pressed
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # check if the user exists
        if user_pass.check_user(request.form['username']):
            return "User already exists"
        else:
            # create a new user
            user_pass.create_user(request.form['username'], request.form['password'])
            return redirect(url_for('/'))
    else:
        return render_template('public/templates/sign_up.html')

# routes when logout is pressed
@app.route('/logout')
def logout():
    return redirect(url_for('/index'))

