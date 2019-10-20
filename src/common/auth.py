import os

from functools import wraps
from flask import request
from flask_restful import abort


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'auth', True):
            return func(*args, **kwargs)

        authenticated = verify_api_key()

        if authenticated:
            return func(*args, **kwargs)

        abort(401)
    return wrapper


def verify_api_key():
    if request.headers.get('x-api-key') and \
            request.headers.get('x-api-key') == os.getenv('API_KEY'):
        return True

    return False
