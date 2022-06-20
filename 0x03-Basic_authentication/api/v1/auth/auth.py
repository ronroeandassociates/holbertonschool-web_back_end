#!/usr/bin/env python3
"""
 create a class Auth: to manage the API authentication
"""

from flask import request
from typing import List, TypeVar

class Auth():

    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str] = []) -> bool:
        """
        require_auth public method
        """
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:

        """authorization_header public method
    """
    if request is None:
        request = request

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user public method
        """
        if request is None:
            request = request
        return None
