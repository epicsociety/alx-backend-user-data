#!/usr/bin/env python3
""" Basic Auth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Authentication """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # noqa: E501
        """ Return the Base64 part of header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        token = authorization_header.split(" ")[-1]
        return token
