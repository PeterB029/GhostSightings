from flask_app import app
from flask_app.controllers import users, sightings, comments, believers, non_believers

if __name__ == '__main__':
    app.run(debug=True)