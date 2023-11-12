#!/usr/bin/env python3
""" Session auth module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """A new authentication mechanism """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create a Session ID for a user_id """
        if user_id and isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return user id based on a session id"""
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id, None)
        return None
