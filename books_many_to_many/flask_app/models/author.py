
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import book
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Author:
    db = "books" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = None
        self.all_books = None
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Author Models
    @classmethod
    def create_author(cls, data):
        query = """
        INSERT INTO authors (name, created_at, updated_at)
        VALUES (%(name)s, NOW(),NOW())
        ;
        """
        connectToMySQL(cls.db).query_db(query,data)
        return



    # Read Author Models
    @classmethod
    def get_one_author(cls,data):
        query = """
        SELECT * FROM authors
        WHERE id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        one_author = cls(results[0])
        return one_author
    
    @classmethod
    def get_all_authors(cls):
        query = """
        SELECT * FROM authors
        ;
        """
        all_authors = []
        results = connectToMySQL(cls.db).query_db(query)
        for author in results:
            all_authors.append(cls(author))
        print("Info getting sent back by get_all_authors", all_authors)
        return all_authors

    @classmethod
    def get_one_author_and_favorites(cls,data):
        query = """
        SELECT * FROM authors
        LEFT JOIN favorites
        ON authors.id = favorites.author_id
        JOIN books
        ON favorites.book_id = books.id
        WHERE authors.id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        one_author = cls(results[0])
        one_author.favorites = book.Book.populate_favorites(results)
        return one_author

    # Update Author Models



    # Delete Author Models
    
    
    # TEST
