from .user import *
from .exceptions import *
from .config import config, _db

from importlib import import_module

_api_mains = []
_auths = []

def api_main(*states):
    """Decorator to use for API main loop"""
    def decorator(fn):
        _api_mains.append(fn)

        return fn
    return decorator

def _createUserObj(username, password, register):
    error = None

    for auth in _auths:
        try:
            return auth.User(_db, username, password, register)
        except Exception as e:
            error = e

    if error:
        raise error

def authenticate(username, password):
    return _createUserObj(username, password, False)

def register(username, password):
    return _createUserObj(username, password, True)

def do_imports():
    for auth in config["Core"]["auth"]:
        _auths.append(import_module("auth." + auth))

    for api in config["Core"]["api"]:
        import_module("api." + api)
