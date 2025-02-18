#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""


from flask import Flask, jsonify, request
app = Flask(__name__)
users =  {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def user_get():
    return jsonify(list(users.keys()))


@app.route("/status")
def statu():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def user_add():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
