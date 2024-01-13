# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    DB = 'first_flask'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        friends = []
        results = connectToMySQL(cls.DB).query_db(query) # The query always returns a list of dictionaries, think [{...},{...}] and these entries are locations in memory.
        for person in results:
            friends.append(cls(person))
        return friends

    @classmethod
    def get_one(cls, data):
        query = """
            SELECT *
            FROM friends
            WHERE id = %(id)s
            ;
        """
        that_one_friend = connectToMySQL(cls.DB).query_db(query, data) # The query always returns a list of dictionaries, think [{...},{...}] and these entries are locations in memory.
        return cls(that_one_friend[0])
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
        return connectToMySQL('first_flask').query_db(query, data)
    
    @classmethod
    def update(cls, data):
        print("The data looks like this (friends.py line 43)", data)
        query = """
            UPDATE friends
            SET first_name = %(first_name)s, 
            last_name = %(last_name)s, 
            occupation = %(occupation)s
            WHERE id = %(id)s
            ;
        """
        results = connectToMySQL('first_flask').query_db(query, data)
        print("The results of the update are", results)
        return results
    
    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM friends
            WHERE id = %(id)s;
        """
        connectToMySQL('first_flask').query_db(query, data)
        return