#!/usr/bin/env python3
"""
User model and authentication service
"""
from atexit import register
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a new user if email isn't listed"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if a user is valid"""
        try:
            user = self._db.find_user_by(email=email)
            password = password.encode('utf8')
            return checkpw(
              password, user.hashed_password.encode("utf-8")
              )

        except NoResultFound:
            return False


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return hashpw(password.encode(), gensalt())
