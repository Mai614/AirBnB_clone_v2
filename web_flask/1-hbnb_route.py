#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
# Route 1: Display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Route 2: Display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

