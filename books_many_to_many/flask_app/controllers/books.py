from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

# Create Users Controller
@app.route("/author/create", methods=["POST"])
def create_author_frontend():
    author.Author.create_author(request.form)
    return redirect("/")



# Read All Authors Controller

@app.route('/')
def index():
    return redirect("/authors")
    
@app.route('/authors')
def show_all_authors_frontend():
    all_authors = author.Author.get_all_authors()
    return render_template('authors.html', all_authors = all_authors)

# Read One Author Controller

@app.route("/authors/<int:id>")
def show_one_author_frontend(id):
    data = {
        'id' : id
    }
    one_author = author.Author.get_one_author(data)
    return render_template("authors_show.html", one_author = one_author)


# Update Users Controller



# Delete Users Controller



# TEST
@app.route("/test")
def show_one_author_frontend_test():
    data = {
        'id' : 1
    }
    one_author = author.Author.get_one_author_and_favorites_test(data)
    return render_template("test.html", one_author = one_author)

# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')                                   The variable must be in the path within angle brackets
# def index(id):                                            It must also be passed into the function as an argument/parameter
#     user_info = user.User.get_user_by_id(id)              The it will be able to be used within the function for that route
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.

# Render template is a function that takes in a template name in the form of a string, then any number of named arguments containing data to pass to that template where it will be integrated via the use of jinja
# Redirect redirects from one route to another, this should always be done following a form submission. Don't render on a form submission.