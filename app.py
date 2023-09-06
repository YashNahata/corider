from flask import Flask
from flask_cors import CORS
import os
from api import users

app = Flask(__name__)
app.app_context().push()
CORS(app)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

app.register_blueprint(users.users_api, url_prefix="/users")

if __name__ == '__main__':
    with app.app_context():
        app.run()