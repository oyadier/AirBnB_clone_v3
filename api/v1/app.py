#!/usr/bin/python3
"""Creating a api using flask framework"""


from flask import Flask, jsonify, make_response
from models import storage
from flask_cors import CORS
from api.v1.views.index import index_view
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.string_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    "for forward routing"
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """
        method to handle Page Not found error
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    hbnb_host = getenv('HBNB_API_HOST')
    hbnb_port = getenv('HBNB_API_PORT')
    app.run(host=hbnb_host, port=hbnb_port,
            threaded=True, debug=True)
