_api_mains = []

def api_main(*states):
    def decorator(fn):
        _api_mains.append(fn)

        return fn
    return decorator

from .user import *
from .exceptions import *
