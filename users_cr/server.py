from flask import Flask, render_template, session, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/read")

@app.route("/read")
def read():
    returned_dictionary = Friend.get_all()
    all_friends = []
    for item in returned_dictionary:
        all_friends.append(item)
        print(item.first_name, "was added to all_friends")
    return render_template("read.html", all_friends = all_friends)

@app.route("/create", methods=["POST","GET"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        data = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "occupation" : request.form['occupation']
        } # This is the data I will use to construct the results of the search.
        Friend.create(data)
        return redirect("/")
        
@app.route("/update", methods=["POST"])
def update():
    Friend.update(request.form)
    return redirect('/')
        
@app.route("/delete/<int:id>")
def delete(id):
    data = {
        'id' : id
    }
    Friend.delete(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)