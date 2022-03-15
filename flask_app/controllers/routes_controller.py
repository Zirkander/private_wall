from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.user_model import User
from flask_app.models.message_model import Message


@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/login')
    messages = Message.get_all_messages_by_id(session['uuid'])

    # This is a fringe case incase there is ever a time when I don't have messages in the database (Like when a new user is created)
    if messages != []:

        # print(messages)
        context = {
            "user": User.get_one(session['uuid']),
            "all_users": User.get_all(),
            "messages": messages
        }
    else:
        context = {
            "user": User.get_one(session['uuid']),
            "all_users": User.get_all(),
            "messages": messages
        }

    return render_template('dashboard.html', **context)
