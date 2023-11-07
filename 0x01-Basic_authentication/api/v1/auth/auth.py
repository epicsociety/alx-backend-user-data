#!/usr/bin/env python3
"""
Class auth
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ manage paths"""
        return False
    

    def authorization_header(self, request=None) -> str:
        """ handles API authetication """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ flask request object """
        return None
