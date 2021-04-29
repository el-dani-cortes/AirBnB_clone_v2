#!/usr/bin/python3
"""
My firts module using flask web framework
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    Function that route to print a specific string
    """
    return 'Hello, HBNB!'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
