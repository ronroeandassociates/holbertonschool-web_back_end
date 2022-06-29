#!/usr/bin/env python3
"""
User model and authentication service
"""
from atexit import register
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


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
        """Validate a user login"""
        try:
            user = self._db.find_user_by(email=email)
            passwrd = password.encode('utf-8')
            return checkpw(passwrd, user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str, password: str) -> bool:
        """Create a new session for a user"""
        try:
            user = self._db.find_user_by(email=email)
            passwrd = password.encode('utf-8')
            if checkpw(passwrd, user.hashed_password):
                session_id = str(uuid.uuid4())
                user.session_id = session_id
                self._db.update_user(user.id, session_id=session_id)
                return session_id
            else:
                raise ValueError("Invalid password")
        except Exception:
            raise ValueError("Invalid email")


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return hashpw(password.encode(), gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID"""
    return str(uuid.uuid4())
