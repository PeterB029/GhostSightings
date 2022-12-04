from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'ghost_sightings_schema'

class Non_believer:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_non_believer(cls):
        query = "SELECT * FROM non_believers"
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_num_non_believers(cls, data):
        query = "SELECT COUNT(sighting_id) FROM non_believers"
        results = connectToMySQL(db).query_db(query, data)
        return results[0]['COUNT(sighting_id)']
    
    @classmethod
    def add_non_believer(cls, data):
        query = "INSERT INTO non_believers (user_id, sighting_id) VALUES (%(user_id)s, %(sighting_id)s)"
        results = connectToMySQL(db).query_db(query, data)
        return results 

    @classmethod
    def remove_non_believer(cls, data):
        query = "DELETE FROM non_believers WHERE user_id=%(user_id)s  AND sighting_id=%(sighting_id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results