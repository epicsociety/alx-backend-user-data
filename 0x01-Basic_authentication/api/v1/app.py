#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from api.v1.auth.auth import Auth
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None


if getenv("AUTH_TYPE") == "auth":
    auth = Auth()
if getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


def before_request():
    """ filter each request """

    if auth is None:
        return
    allowed_paths = ['/api/v1/status/',
                     '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth.require_auth(request.path, allowed_paths):
        return
    authorization_header = auth.authorization_header(request)
    if not authorization_header:
        abort(401)
    if not auth.current_user(request):
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def request_unauthorized(error) -> str:
    """ Request unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_access(error) -> str:
    """ Forbidden access handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
