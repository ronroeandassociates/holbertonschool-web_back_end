#!/usr/bin/env python3
"""
User model and authentication service
"""
from atexit import register
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
       """Register a new user"""
       try:
        self.db.find_user_by(email=email)
        raise ValueError(f"User{email} already exists")
       except NoResultFound:
        hashed_password = hashpw(password)
        user = self._db.add_user(email, hashed_password)
        return user

def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return hashpw(password.encode(), gensalt())
