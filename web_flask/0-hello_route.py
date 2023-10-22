#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

# Import the Flask class from the flask module
from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/"). The route decorator binds a function
# to a URL and defines the response to be sent back when that URL is accessed.
# The option strict_slashes=False allows both '/path' and '/path/' to work.
@app.route('/', strict_slashes=False)
def hello():
    # Return the string "Hello HBNB!" as the response when the root URL is accessed
    return "Hello HBNB!"

# The following block checks if the script is being run directly. If it is,
# the Flask development server is started, listening on all network interfaces
# (host='0.0.0.0') and port 5000. This allows the web application to be accessible
# externally.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
