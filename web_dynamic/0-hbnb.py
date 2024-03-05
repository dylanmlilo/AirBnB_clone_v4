#!/usr/bin/python3
""" Initiates a Flash Web Application """
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def end_db(error):
    """ Ends the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    state_cities = []

    for state in states:
        state_cities.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=states_cities,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)