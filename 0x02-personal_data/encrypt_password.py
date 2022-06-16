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
