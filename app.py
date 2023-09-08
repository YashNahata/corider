from flask import Flask
from flask_cors import CORS
import os
from api.users import Users, AllUsers
from flask_restful import Api

app = Flask(__name__)
app.app_context().push()
CORS(app)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

api = Api(app)
api.add_resource(AllUsers, '/users/', '/users/')
api.add_resource(Users, '/user/', '/user/<string:user_id>')

if __name__ == '__main__':
    with app.app_context():
        app.run()