#!/usr/bin/env python3
"""
Class auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication system """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Manage paths"""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path.rstrip('/')):
                if '*' in excluded_path:
                    prefix = excluded_path.rstrip('*').rstrip('/')
                    if path == prefix or path.startswith(prefix):
                        return False
                else:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Handle API authetication """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        return header if header else None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Flask request object """
        return None
