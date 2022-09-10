#!/usr/bin/env python3
"""Module for API authentication"""


from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """API authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns false if path is in excluded_paths"""
        if path is None or excluded_paths is None:
            return True

        return path not in excluded_paths and f"{path}/" not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Returns flask request or none if no header"""
        if request is None or request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user or none"""
        return None

    def session_cookie(self, request=None):
        """Returns session cookie or none"""
        if request is None:
            return None
        cookie_name = getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
