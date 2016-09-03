from flask import Flask

app = Flask(__name__)

import basic_auth.RESTapi, basic_auth.WebPage
    