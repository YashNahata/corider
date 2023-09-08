from flask import Flask, request, Blueprint, make_response
from flask_restful import Resource, Api, url_for
from db import users

app = Flask(__name__)
api_bp1 = Blueprint('users_api', __name__)
api_bp2 = Blueprint('all_users_api', __name__)
class Users(Resource):
    def post(self):
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]
        user_data = { "name": name, "email": email, "password": password }
        return users.create_user(user_data)

    def get(self, user_id):
        return users.find_user(user_id)
    
    def put(self, user_id):
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]
        user_data = { "name": name, "email": email, "password": password, "id": user_id }
        return users.update_user(user_id, user_data)

    def delete(self, user_id):
        return users.delete_user(user_id)

class AllUsers(Resource):
    def get(self):
        return users.get_all_users()