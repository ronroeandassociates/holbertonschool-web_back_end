#!/usr/bin/env python3
"""
Module for basic authentication
"""

from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """
    Basic authentication class
    """
    def __init__(self) -> None:
        """
        Initialize the class
        """
        super().__init__()
