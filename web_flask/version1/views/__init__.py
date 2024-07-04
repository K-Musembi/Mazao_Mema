#!/usr/bin/python3
"""create blueprint"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="")

from web_flask.version1.views.index import *
