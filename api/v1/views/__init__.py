#!/usr/bin/python3
"""
   Creates a Blueprint instance with url_prefix set to /api/v1.
"""


from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if app_views is not None:
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.amenities import *
    from api.v1.views.users import *
    rom api.v1.views.places import *
