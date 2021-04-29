#!/usr/bin/python3
"""
My firts module using flask web framework
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    Function that route to return 'Hello, HBNB'
    """
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    Function that route to return 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_programming(text):
    """
    Function that routes to return a variable string,
    acording a variable pass in the url.
    """
    text = text.replace('_', ' ')
    return 'C %s!' % text


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
