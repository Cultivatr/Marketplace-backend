from flask import request
from google.oauth2 import id_token
from google.auth.transport import requests
from functools import wraps

def authorized(fn):
    @wraps(fn)
    def _wrap(*args, **kwargs):
        try:
            idinfo = id_token.verify_oauth2_token(request.headers['Authorization'], requests.Request(), '441538396161-96k3lmo0iv81qq4b5h0p6u21iefi0ia7.apps.googleusercontent.com')
        except:
            idinfo = 'unauthorized'
        return fn(idinfo=idinfo, *args, **kwargs)
    return _wrap