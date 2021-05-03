#!/usr/bin/python3
"""
My firts module using flask web framework
"""
from flask import Flask, escape, render_template
import models
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """
    Function that display a HTML with list of states
    """
    states_dict = {}
    all_states = models.storage.all(State)
    for key, value in all_states.items():
        states_dict[value.name] = value
    return render_template('9-states.html', states_dict=states_dict)


@app.route('/states/<id>', strict_slashes=False)
def states_and_cities_by_id(id):
    """
    Function that display a HTML with states id and its cities
    """
    state_object = None
    all_states = models.storage.all(State)
    for key, value in all_states.items():
        state_id = key.split('.')
        if state_id[1] == id:
            state_object = value
    return render_template('9-states.html', id=id, state_object=state_object)


@app.teardown_appcontext
def close_connection_db(exception):
    """
    Method to close connection with database
    """
    models.storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
