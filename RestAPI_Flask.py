import tkinter as tk
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"user_id": "0", "user_name": "a", "user_salary": "100"}
]


@app.route("/")
def index():
    return "Flipr internship task..!"


@app.route("/users", methods=['GET'])
def get():
    return jsonify({"Users": users})


@app.route("/users/<int:user_id>", methods=['GET'])
def get_by_user(user_id):
    return jsonify({"users": users[user_id]})


@app.route("/users", methods=['POST'])
def create():
    new = {"user_id": "1", "user_name": "b", "user_salary": "200"};
    users.append(new)
    return jsonify({"New_User": new})


@app.route("/users/<int:user_id>", methods=['PUT'])
def user_update(user_id):
    users[user_id]['user_salary'] = "500"
    return jsonify({"users": users[user_id]})


@app.route("/users/<int:user_id>", methods=['DELETE'])
def get_by_user(user_id):
    users.remove(users[user_id])
    return jsonify({"Deleted": True})


if __name__ == "__main__":
    app.run(debug=True)