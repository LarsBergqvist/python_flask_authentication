from basic_auth import app
from flask import request, jsonify
import functools

def ok_user_and_password(username, password):
    return username == app.config['USERNAME'] and password == app.config['PASSWORD']

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Main"'

    return resp

def requires_authorization(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not ok_user_and_password(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
