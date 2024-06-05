#!/usr/bin/python3
"""
    starts a Flask web application
    web application listens on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tearDown(exception):
    """
        remove the current SQLAlchemy Session
        after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def listState():
    """
        List states in the storage alphabetically
    """
    all_states = list()
    states = storage.all(State)
    for state in states:
        all_states.append(state)
    return render_template("7-states_list.html",
                           all_states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
