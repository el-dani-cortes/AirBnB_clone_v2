#!/usr/bin/python3
"""
My firts module using flask web framework
"""
from flask import Flask, escape, render_template
import models
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Function that display a HTML with list of states
    """
    states_dict = {}
    amenities_list = []
    all_states = models.storage.all(State)
    all_amenities = models.storage.all(Amenity)
    for key, value in all_amenities.items():
        amenities_list.append(value.name)
    amenities_list.sort()
    for key, value in all_states.items():
        states_dict[value.name] = value
    return render_template('10-hbnb_filters.html', states_dict=states_dict, amenities_list=amenities_list)


@app.teardown_appcontext
def close_connection_db(all_states):
    """
    Method to close connection with database
    """
    if all_states is not None:
        storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
