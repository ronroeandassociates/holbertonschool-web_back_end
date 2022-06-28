#!/usr/bin/env python3
"""
User model and authentication service
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return hashpw(password.encode(), gensalt())
