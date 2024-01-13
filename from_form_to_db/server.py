from flask import Flask, render_template, session, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    friends = Friend.get_all()
    # If I wanted to get a friend by id number or name, what would that look like?
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/process", methods=['POST'])
def process():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    Friend.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    
    
