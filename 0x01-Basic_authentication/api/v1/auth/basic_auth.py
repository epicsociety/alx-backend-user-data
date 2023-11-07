#!/usr/bin/env python3
""" Basic Auth module
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:  # noqa: E501
        """ Returns the decoded value of a Base64 string """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            decoded_str = decoded.decode('utf-8')
            return decoded_str
        except Exception:
            return None
