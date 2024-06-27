#!/usr/bin/python3
"""the main flask file"""

from web_flask.version1.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS

main_app = Flask(__name__)
main_app.register_blueprint(app_views)
cors = CORS(main_app, resources={r"/*": {"origins": "*"}})


@main_app.errorhandler(404)
def not_found(error):
    """custom error handler"""
    return make_response(jsonify({"error": "not found"}), 404)


if name == "__main__":
    """main function"""
    main_app.run(host="0.0.0.0", port=5001, threaded=True)
