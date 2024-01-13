from flask import Flask, render_template, session, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "GET":
        friends = Friend.get_all()
        return render_template("index.html", all_friends = friends)
    elif request.method == "POST":
        result = int(request.form['id_num'])
        displayed_result = Friend.get_one('first_flask', result)
        print(displayed_result)
        return render_template("result.html", all_friends = displayed_result)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/process", methods=['POST'])
def process():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "occupation" : request.form["occ"]
    }
    Friend.save(data)
    return redirect('/')

@app.route("/search")
def search():
    return render_template('search.html')

@app.route('/search/process', methods=["POST"])
def process_search():
    id = int(request.form['id'])
    print(id)
    that_one_friend = Friend.get_one(id)
    print("that_one_friend = ", that_one_friend)
    friends = []
    friends.append(that_one_friend)
    return render_template('returned_search.html', all_friends = friends, method="POST")

if __name__ == "__main__":
    app.run(debug=True)
    
    
