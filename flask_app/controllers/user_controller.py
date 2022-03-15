from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/user/create', methods=['POST'])
def new_user():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        return redirect('/login')

    hash_pw = bcrypt.generate_password_hash(request.form['password'])
    info = {
        **request.form,
        "hash_pw": hash_pw
    }

    user_id = User.create(info)
    session['uuid'] = user_id
    return redirect('/')
