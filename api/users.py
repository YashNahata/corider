from flask import Flask, request, Blueprint
from db import users
users_api = Blueprint('users_api', __name__)

@users_api.route("/", methods=['GET'])
def getUsers():
    return users.get_all_users()

@users_api.route("/<user_id>", methods=['GET'])
def getUser(user_id):
    return users.find_user(user_id)

@users_api.route("/", methods=['POST'])
def createUser():
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]
    user_data = { "name": name, "email": email, "password": password }
    return users.create_user(user_data)

@users_api.route("/<user_id>", methods=['PUT'])
def updateUser(user_id):
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]
    user_data = { "name": name, "email": email, "password": password, "id": user_id }
    return users.update_user(user_id, user_data)

@users_api.route("/<user_id>", methods=['DELETE'])
def deleteUser(user_id):
    return users.delete_user(user_id)