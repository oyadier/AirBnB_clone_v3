#!/usr/bin/python3
'''
Create a route `/status` on the object app_views.
'''


from flask import jsonify, Blueprint
from api.v1.views import app_views
from models import storage
from models.state import State


index_view = Blueprint('index_view', __name__,
                       template_folder='view', url_prefix='/api/v1')


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    '''
    Returns a JSON response for RESTful API health.
    '''
    response = {'status': 'OK'}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def obj_status():
    '''
        Create endpoint that retrieves the number of each objects by type.
    '''
    classes = {
        "amenities": 'Amenity',
        "cities": 'City',
        "places": 'Place',
        "reviews": 'Review',
        "states": 'State',
        "users": 'User'
    }
    cout_dict = {}
    for cls in classes:
        cout_dic[cls] = storage.count(classes[cls])
    return jsonify(cout_dict)
