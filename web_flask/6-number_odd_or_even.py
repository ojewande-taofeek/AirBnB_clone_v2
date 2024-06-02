#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask, abort, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Returns Hello"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    if text is None:
        abort(404)
    if '_' in text:
        text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    if '_' in text:
        text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def numb(n):
    if not isinstance(n, int):
        abort(404)
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number(n):
    if not isinstance(n, int):
        abort(404)
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    if not isinstance(n, int):
        abort(404)
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
