from basic_auth import app
from basic_auth.requires_authorization import requires_authorization
from basic_auth.messages import get_secret_message
from flask import jsonify

@app.route('/api/secret')
@requires_authorization    
def api_secret():
    return jsonify({'message':get_secret_message()})
