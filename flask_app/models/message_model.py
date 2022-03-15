# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import date, datetime
import humanize
import re
# model the class after the friend table from our database

DATABASE = 'privateWall'


class Message:  # update this section with what is standard in the db
    def __init__(self, data):
        self.id = data['message_id']
        self.content = data['content']
        self.receiver_id = data['receiver_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.User_id = data['User_id']

    def timeago(created_at):
        time = humanize.naturaltime(datetime.datetime.now() - created_at)
        # time = created_at

        return time


# C


    @classmethod
    def create(cls, info):
        query = 'INSERT INTO message (content, receiver_id, User_id) VALUES (%(content)s,%(receiver_id)s, %(User_id)s);'

        data = {
            "content": info['content'],
            "receiver_id": info['receiver_id'],
            "User_id": info['User_id']
        }
        new_message_id = connectToMySQL(DATABASE).query_db(query, data)

        return new_message_id

# R
    # Now we use class methods to query our database
    @classmethod
    def get_all_messages_by_id(cls, ID):
        query = 'select message.message_id, message.content, message.receiver_id, message.created_at, message.User_id, users.first_name, users.last_name from message left join users on message.User_id = users.user_id where message.receiver_id = %(ID)s order by message.created_at;'
        data = {
            "ID": ID
        }
        results = connectToMySQL(DATABASE).query_db(query, data)
        # Create an empty list to append our instances of friends
        messages = []
        # print(results)
        for message in results:
            time = Message.timeago(message['created_at'])
            # messages.append("time": time)
            messages.append({'time': time})
            messages.append(message)
        return messages


# U

    @classmethod
    def update_one():
        pass


# D


    @classmethod
    def delete_one():
        pass

    @staticmethod
    def validate_message(message):
        is_valid = True
        if len(message['content']) < 5:
            flash("Message has to be longer than 5 characters!")
            is_valid = False
        return is_valid
