#!/usr/bin/python3
"""the main routes"""

from models.county import County
from models.consultant import Consultant
from models.input_dealer import InputDealer
from models.buyer import Buyer
from web_flask.version1.views import app_views
from flask import render_template

counties = [County, Consultant, InputDealer, Buyer]


@app_views.route("/", strict_slashes=False)
def index():
    """home page"""
    return render_template("index.html")


@app_views.route("/<county>", strict_slashes=False)
def choose_service(county):
    """choose county"""
    if county.lower() in ("machakos", "kiambu", "meru", "kajiado", "muranga"):
        return render_template("choose.html", name=county.capitalize())
    else:
        return render_template("not_found.html")


@app_views.route("/about", strict_slashes=False)
def about():
    """about page"""
    return render_template("about.html")


@app_views.route("/contacts", strict_slashes=False)
def contacts():
    """contact us page"""
    return render_template("contacts.html")
