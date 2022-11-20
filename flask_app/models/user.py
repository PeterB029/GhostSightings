from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
db = 'ghost_sightings_schema'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, username, email, password) VALUES (%(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s);"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results[0]

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, username=%(username)s, email=%(email)s, password=%(password)s WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s"
        email_matches = connectToMySQL(db).query_db(query, {"email": user['email']})
        if len(email_matches) > 0:
            flash("Email is already registered")
            is_valid = False
        query = "SELECT * FROM users WHERE username = %(username)s"
        user_matches = connectToMySQL(db).query_db(query, {"username": user['username']})
        if len(user_matches) > 0:
            flash("Username is already being used. Plesae Try another name.")
            is_valid = False
        if len(user['first_name']) < 3:
            flash('First name must be at least 3 characters long.')
            is_valid = False
        if len(user['last_name']) < 3:
            flash('Last name must be at least 3 characters long.')
            is_valid = False
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters long.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email Address!')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must be at least 8 characters long.')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('Passwords do not match!')
            is_valid = False
        return is_valid

