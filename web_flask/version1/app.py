#!/usr/bin/python3
"""the main flask file"""

from web_flask.version1.views import app_views
from flask import Flask, make_response, jsonify, session
from flask_cors import CORS
from models import db
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

app.secret_key = os.urandom(24)

#connect to mysql database username:password@host/db_name. (other options: sqlite, postgresql)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://admin:admindb@localhost/mazao_db"

#prevent automatic update of database objects to save memory. Define methods instead
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

#import the models before calling db.create_all()
with app.app_context():
    from models import County, Consultant, InputDealer, Buyer
    db.create_all()

#register blueprint for code reusability
app.register_blueprint(app_views)

#security: define who can access which resource. In this case, all origins, all resources
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """custom error handler"""
    return make_response(jsonify({"error": "not found"}), 404)


if __name__ == "__main__":
    """main function"""
    app.run(host="0.0.0.0", port=5001, threaded=True)
