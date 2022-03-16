# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# model the class after the friend table from our database

DATABASE = 'privateWall'


class User:  # update this section with what is standard in the db
    def __init__(self, data):
        self.id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']


self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
# C

    @classmethod
    def create(cls, info):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(hash_pw)s);'
        data = {
            "first_name": info['first_name'],
            "last_name": info['last_name'],
            "email": info['email'],
            "hash_pw": info['hash_pw']
        }
        new_user_id = connectToMySQL(DATABASE).query_db(query, data)
        return new_user_id

# R
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users order by first_name;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(
            query)  # Change first_flask to the db schema
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, ID):
        query = "select * from users where user_id = %(ID)s;"
        data = {
            "ID": ID
        }
        return cls(connectToMySQL(DATABASE).query_db(query, data)[0])

    @classmethod
    def get_one_by_email(cls, email):
        query = "SELECT * FROM users where email = %(email)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        data = {
            "email": email
        }
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results


# U


    @classmethod
    def update_one():
        pass


# D

    @classmethod
    def delete_one():
        pass

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First name must be longer than 3 characters")
            is_valid = False

        if len(user['last_name']) < 3:
            flash("Last name must be longer than 3 characters")
            is_valid = False

        if len(user['email']) < 3:
            flash("Email must be longer than 3 characters")
            is_valid = False
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(user['password']) < 8:
            flash("Password must be longer than 6 characters")
            is_valid = False

        if user['password'] != user['confirm_password']:
            flash("Password must match confirmation")
            is_valid = False
        return is_valid
