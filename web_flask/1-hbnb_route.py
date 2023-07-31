#!/usr/bin/python3
"""Flask web application framework
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello():
    """This is the view
    function
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this is the second
    view function
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
