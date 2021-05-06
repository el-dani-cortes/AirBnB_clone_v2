#!/usr/bin/python3
"""
My firts module using flask web framework
"""
from flask import Flask, escape, render_template
import models
from models.state import State
from models.place import Place
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def filters():
    """
    Function that display a HTML that bring states, cities, amenities
    and places 
    """
    states_dict = {}
    amenities_list = []
    all_states = models.storage.all(State)
    all_amenities = models.storage.all(Amenity)
    all_places = models.storage.all(Place)
    for key, value in all_amenities.items():
        amenities_list.append(value.name)
    amenities_list.sort()
    for key, value in all_states.items():
        states_dict[value.name] = value
    return render_template('100-hbnb.html', states_dict=states_dict, amenities_list=amenities_list, all_places=all_places)


@app.teardown_appcontext
def close_connection_db(exception):
    """
    Method to close connection with database
    """
    models.storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
