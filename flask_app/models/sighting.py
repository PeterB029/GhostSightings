from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'ghost_sightings_schema'

class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.location = data['location']
        self.date = data['date']
        self.time = data['time']
        self.description = data['description']
        self.intensity = data['intensity']
        self.num_of_activities = data['num_of_activities']
        self.reaction = data['reaction']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_sighting(cls, data):
        query = "INSERT into sightings (title, location, date, time, description, intensity, num_of_activities, reaction, user_id) VALUES (%(title)s, %(location)s, %(date)s, %(time)s, %(description)s, %(intensity)s, %(num_of_activities)s, %(reaction)s, %(user_id)s)"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def update_sighting(cls, data):
        query = "UPDATE sightings SET title=%(title)s, location=%(location)s, date=%(date)s, time=%(time)s, description=%(description)s, intensity=%(intensity)s, num_of_activities=%(num_of_activities)s, reaction=%(reaction)s WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_one_sighting_by_user(cls, data): #View Sighting Page
        query = "SELECT * FROM sightings JOIN users ON users.id=sightings.user_id WHERE sightings.id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results[0]

    @classmethod
    def get_all_sightings_by_users(cls): #Main Page
        query = "SELECT * FROM sightings JOIN users ON users.id=sightings.user_id"
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_all_sightings_by_user(cls, data): #User Page
        query = "SELECT * FROM sightings JOIN users ON users.id=sightings.user_id WHERE users.id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_sighting(cls, data):
        query = "DELETE FROM sightings WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_sighting(sighting):
        is_valid = True
        if len(sighting['title']) < 3:
            flash("Title must be at least 3 characters long")
            is_valid = False
        if len(sighting['location']) < 3:
            flash("Location must be at least 3 characters long")
            is_valid = False
        if not sighting['date']:
            flash("Date must be filled in")
            is_valid = False
        if not sighting['time']:
            flash("Time must be filled in")
            is_valid = False
        if len(sighting['description']) < 3:
            flash("Description must be at least 3 characters long")
            is_valid = False
        if int(sighting['num_of_activities']) < 1:
            flash("Number of Activities must be at least 1")
            is_valid = False
        if len(sighting['reaction']) < 3:
            flash("Reaction must be at least 3 characters long")
            is_valid = False
        return is_valid
