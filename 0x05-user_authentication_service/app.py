#!/usr/bin/env python3
"""app Module using Flask"""
from flask import Flask, request, jsonify, abort, redirect
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
    """Route for login a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not (AUTH.valid_login(email=email, password=password)
            ) or not email or not password:
        abort(401)

    session_id = AUTH.create_session(email=email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Route for log out a user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user and session_id:
        AUTH.destroy_session(session_id)
        return redirect('/')

    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """Route for profile of user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user and session_id:
        return jsonify({'email': user.email}), 200

    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Route to receive reset password token"""
    try:
        email = request.form.get('email')
        token = AUTH.get_reset_password_token(email)
        return jsonify({'email': email, 'reset_token': token}), 200

    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Route to update password"""
    try:
        email = request.form.get('email')
        token = request.form.get('reset_token')
        new_password = request.form.get('new_password')
        AUTH.update_password(token, new_password)
        return jsonify({'email': email, 'message': 'Password updated'}), 200

    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
