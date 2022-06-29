#!/usr/bin/env python3
from flask import Flask, request, jsonify, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /status
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def new_user() -> str:
    """If user no exist register user"""
    # Get data from form request, change to request.get_json() for body
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        new_user = AUTH.register_user(email, password)
        if new_user is not None:
            return jsonify({
                "email": new_user.email,
                "message": "user created"
            })
    except ValueError:
        return jsonify({
            "message": "email already registered"
            }), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Route for loggin in a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not (AUTH.valid_login(email=email, password=password)
            ) or not email or not pw:
        abort(401)

    session_id = AUTH.create_session(email=email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
