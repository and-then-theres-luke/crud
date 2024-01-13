from flask_app import redirect, request
from flask_app.models import burger

@app.route('/burgers')
def burgers():
    return render_template('results.html', burgers = burger.Burger.get_all())

@app.route('/create/burger',methods=['POST'])
def create_burger():
	data = {
        "name" : request.form['name'],
        "bun" : request.form['bun'],
        "meat" : request.form['meat'],
        "calories" : request.form['calories']
	}
	burger.Burger.save(data)
	return redirect('/burgers')