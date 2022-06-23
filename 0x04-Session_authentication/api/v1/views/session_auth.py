#!/usr/bin/env python3
"""Module of session_id views
"""
from flask import request, jsonify, abort, make_response
from models.user import User
from os import getenv
from api.v1.views import app_views
from api.v1.auth.session_auth import SessionAuth


def login():
    """Handles log in"""

    email = request.form.get('email')

    if email is None:
        return (jsonify({"error": "email missing"}), 400)
    password = request.form.get('password')

    if password is None:
        return (jsonify({"error": "password missing"}), 400)

    search = User.search({'email': email})

    if len(search) == 0:
        return (jsonify({"error": "no user found for this email"}), 404)

    for user in search:
        if not user.is_valid_password(password):
            return (jsonify({"error": "wrong password"}), 401)

        else:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return (response)

@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ deletes session"""
    from api.v1.app import auth
    if (auth.destroy_session(request)):
        return jsonify({}, 200)

    abort(404)
