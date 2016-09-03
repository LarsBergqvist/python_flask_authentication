from basic_auth import app
from basic_auth.requires_authorization import requires_authorization
from basic_auth.messages import get_secret_message
from flask import render_template

@app.route('/')
@requires_authorization
def index():
    return render_template('index.html', message=get_secret_message())
    