from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.user_model import User
from flask_app.models.message_model import Message


@app.route('/message_send', methods=['POST'])
def send_message():
    if 'uuid' not in session:
        return redirect('/login')
    is_valid = Message.validate_message(request.form)
    print(request.form)
    if not is_valid:
        return redirect('/dashboard')

    print(request.form['rec_id'])
    receiver_id = int(request.form["rec_id"])

    info = {
        **request.form,
        "User_id": session['uuid'],
        "receiver_id": receiver_id
    }
    new_message = Message.create(info)
    print(new_message)

    return redirect('/dashboard')
