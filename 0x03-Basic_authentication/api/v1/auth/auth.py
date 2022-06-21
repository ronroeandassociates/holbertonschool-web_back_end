#!/usr/bin/env python3
"""
 create a class Auth: to manage the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth():

    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth function
        """
        if excluded_paths is None or excluded_paths == '':
            return True
        if path is not None:
            if path[len(path) - 1] is not '/':
                path += '/'
        if path is None:
            return True
        for item in excluded_paths:
            asterisk = item.find("*")
            if asterisk != -1 and len(path) >= len(item):
                pathcpy = path[: asterisk]
                if pathcpy == item[: asterisk]:
                    return False
            elif path == item:
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
