#!/usr/bin/env python3
"""
Class auth
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Authentication system """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Manage paths"""
        return False

    def authorization_header(self, request=None) -> str:
        """ Handle API authetication """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object """
        return None
