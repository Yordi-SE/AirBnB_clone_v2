#!/usr/bin/python3
"""Flask web application framework
"""
from flask import Flask, render_template
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """This is the third
    view function
    """
    text = text.replace('_', " ")
    return render_template('c_route.html', text=text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text=None):
    """This is the fourth
    view function
    """
    if text:
        text = text.replace("_", " ")
    return render_template('python.html', text=text)


@app.route('/number/<int:n>', strict_slashes=False)
def numba(n):
    """This is the fifth
    view function
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
