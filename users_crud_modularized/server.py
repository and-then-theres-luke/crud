from flask_app import app
from flask_app.models import friend
from flask_app.controllers import friends




if __name__ == "__main__":
    app.run(debug=True)