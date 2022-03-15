from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def get_all():
    # all_users = User.get_all()
    return redirect('/login')


@app.route('/login')
def login():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('login.html')


@app.route('/process_login', methods=['POST'])
def process_login():
    # get user by email
    list_of_users = User.get_one_by_email(request.form['email'])

    if len(list_of_users) <= 0:
        flash('Please enter correct creds!')
        return redirect('/login')

    user = list_of_users[0]

    if not bcrypt.check_password_hash(user['password'], request.form['password']):
        flash('Invalid Credentials, Please try again!')
        return redirect('/login')

    session['uuid'] = user['user_id']
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
