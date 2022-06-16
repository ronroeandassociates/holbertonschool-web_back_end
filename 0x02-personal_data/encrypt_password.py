#!/usr/bin/env python3
"""
5 Encrypting passwords
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password for storing in a database.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Verifies a password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
