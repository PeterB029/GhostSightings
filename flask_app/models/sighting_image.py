from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Sighting_Image:
    def __init__(self, data):
        self.id = data['id']
        self.image_path = data['image_path']
        # self.image_decription = data['image_description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']