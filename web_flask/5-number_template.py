#!/usr/bin/python3
"""
My firts module using flask web framework
"""
from flask import Flask, escape, render_template

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
    return 'C %s' % text


@app.route('/python', defaults={'text': None}, strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python_programming(text):
    """
    Function that routes to return a variable string,
    acording a variable pass in the url and is optional.
    """
    if text is None:
        return 'Python is cool'
    text = text.replace('_', ' ')
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    """
    Function that routes to a return if the variable is a int.
    """
    return '%s is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def HTML_integer(n):
    """
    Function that display a HTML, if the variable in route is a int.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
