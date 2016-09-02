from flask import Flask, request, jsonify, render_template
from functools import wraps
import sys, getopt

app = Flask(__name__)

def check_auth(username, password):
    return username == app.config['USERNAME'] and password == app.config['PASSWORD']

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/secret/api')
@requires_auth    
def api_secret():
    return jsonify(get_secret_message())

def get_secret_message():
    return ("The secret messages are calling to me endlessly, " +
    "they call to me across the air, " +
    "the messages across the atmosphere, " +
    "they whisper in your ear, they're calling everywhere")

@app.route('/secret')
@requires_auth    
def index():
    return render_template('index.html', message=get_secret_message())

def main(argv):
    user = ''
    password = ''

    try:
        opts, args = getopt.getopt(argv,"u:p:")
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-u"):
            user = arg
        elif opt in ("-p"):
            password = arg

    if len(user) == 0 or len (password) == 0:
        printHelp()
        sys.exit(0)

    print('User name is:',  user)
    print('Password is:', password)
    app.config['USERNAME']=user
    app.config['PASSWORD']=password

def printHelp():
    print('Usage: ',__file__,'-u <user name> -p <password>')
    
if __name__ == '__main__':
    main(sys.argv[1:])
    app.run(debug=False)