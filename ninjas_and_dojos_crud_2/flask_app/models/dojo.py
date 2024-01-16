
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Dojo:
    db = "dojos_and_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = None
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Dojo Models
    @classmethod
    def create_dojo(cls, data):
        query = """
        INSERT INTO dojos (name, created_at, updated_at)
        VALUES (%(name)s,NOW(),NOW())
        ;
        """
        connectToMySQL(cls.db).query_db(query, data)
        return


    # Read Dojo Models
    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT * FROM dojos;
        """
        result = connectToMySQL(cls.db).query_db(query)
        all_dojos = []
        for dojo in result:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = """
        SELECT * FROM dojos 
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        one_dojo = cls(result[0])
        return one_dojo
    



