#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
#comment

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
