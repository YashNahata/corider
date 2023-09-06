from flask import Flask, current_app, g, jsonify
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy
from bson import json_util
import shortuuid

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    return db

db = LocalProxy(get_db)

def get_all_users():
    try:
        response = json_util.dumps(db.users.find({}))
        return response
    except:
        return { "status": "error" }

def find_user(user_id):
    response = json_util.dumps(db.users.find({ "id": user_id }))
    try:
        return { "user": response }
    except:
        return { "status": "error" }

def create_user(user_data):
    user_id = shortuuid.uuid()
    user_data["id"] = user_id
    try:
        response = db.users.insert_one(user_data)
        return { "status": "ok" }
    except:
        return { "status": "error" }

def delete_user(user_id):
    try:
        response = db.users.delete_one({ "id": user_id } )
        return { "status": "ok" }
    except:
        return { "status": "error" }

def update_user(user_id, user_data):
    try:
        response = db.users.update_one({ "id": user_id }, { "$set": user_data })
        return { "status": "ok" }
    except:
        return { "status": "error" }