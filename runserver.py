#!/usr/bin/env python3
import sys, getopt
from basic_auth import app

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
    context = ('ssl.cert', 'ssl.key')
    app.run(host='0.0.0.0', port=80, ssl_context=context) 
