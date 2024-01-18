
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import author
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Book:
    db = "books" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Book Models
    @classmethod
    def create_book(cls, data):
        query = """
        INSERT INTO books (title, num_of_pages, created_at, updated_at)
        VALUES (%(title)s,%(num_of_pages)s, NOW(),NOW())
        ;
        """
        connectToMySQL(cls.db).query_db(query,data)
        return


    # Read Book Models
    @classmethod
    def get_one_book(cls,data):
        query = """
        SELECT * FROM books
        WHERE id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        one_book = cls(results[0])
        return one_book

    @classmethod
    def get_all_books(cls):
        query = """
        SELECT * FROM books
        ;
        """
        all_books = []
        results = connectToMySQL(cls.db).query_db(query)
        for book in results:
            all_books.append(cls(book))
        return all_books

    @classmethod
    def get_all_books_minus_favorites(cls, one_author):
        all_books_ever = Book.get_all_books()
        for one_fav in one_author.favorites:
            #this will iterate for each book in favorites
            for one_book in range(0,len(all_books_ever)-1):
                #remember that this is an integer as we cycle doing comparisons between the fav book and the one book
                if one_fav.title == all_books_ever[one_book].title:
                    all_books_ever.pop(one_book)
                else:
                    pass
        return all_books_ever
                
            
    
    @classmethod
    def populate_favorites(cls,data):
        favorite_books = []
        for book in data:
            favorite_books.append(cls(book))
        return favorite_books


    # Update Book Models



    # Delete Book Models