#!/usr/bin/env python3
"""Auth method
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """  return salted hash input password
    as bytes
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash
