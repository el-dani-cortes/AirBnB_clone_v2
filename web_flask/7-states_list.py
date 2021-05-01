#!/usr/bin/python3
"""
My firts module using flask web framework
"""
from flask import Flask, escape, render_template
import models
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    Function that display a HTML with list of states
    """
    states_dict = {}
    all_states = models.storage.all(State)
    for key, value in all_states.items():
        states_dict[value.name] = value
    return render_template('7-states_list.html', states_dict=states_dict)


@app.teardown_appcontext
def close_connection_db(all_states):
    """
    Method to close connection with database
    """
    if all_states is not None:
        storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
