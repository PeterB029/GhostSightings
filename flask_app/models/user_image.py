from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = "ghost_sightings_schema"

class User_Image:
    def __init__(self, data):
        self.id = data['id']
        self.image_path = data['image_path']
        # self.image_decription = data['image_description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_image_by_user(cls, data):
        query = "SELECT * FROM user_images WHERE user_id=%(user_id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def add_user_image(cls, data):
        query = "INSERT INTO user_images (image_path) VALUES(%(image_path)s)"
        results = connectToMySQL(db).query_db(query, data)
        return results