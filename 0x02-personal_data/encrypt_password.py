#!/usr/bin/env python3
"""
5 Encrypting passwords
User passwords should NEVER be stored in plain text in a database.
Implement a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string.
Use the bcrypt package to perform the hashing (with hashpw).
"""

import bcrypt

def _hash_password(password: str) -> str:
    """
    Hash a password for storing in a database.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
