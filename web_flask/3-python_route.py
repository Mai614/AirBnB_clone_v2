#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that returns a message when accessed
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that returns a specific message when accessed
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route that takes a parameter and returns a message
    """
    text = escape(text).replace('_', ' ')
    return "C {}".format(text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route that takes an optional parameter and returns a message
    """
    text = escape(text).replace('_', ' ')
    return "Python {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

