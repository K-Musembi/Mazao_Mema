#!/usr/bin/python3
"""the main routes"""

from models import County, Consultant, InputDealer, Buyer
from web_flask.version1.views import app_views
from flask import render_template, request, session, url_for
import requests

service_classes = {'consultant': Consultant, 'inputdealer': InputDealer, 'buyer': Buyer}


@app_views.route("/", strict_slashes=False)
def index():
    """home page"""
    return render_template("index.html")


#NB: url parameters (i.e. "/<county>") are used with GET. not suitable for forms
@app_views.route("/county", methods=['POST'], strict_slashes=False)
def choose_service():
    """choose county"""
    county = request.form.get('county')
    if county.lower() in ("machakos", "kiambu", "kajiado"):
        session['county'] = county.capitalize()
        return render_template("choose.html", name=county.capitalize())
    return render_template("not_found.html")


@app_views.route("/about", strict_slashes=False)
def about():
    """about page"""
    return render_template("about.html")


@app_views.route("/contacts", strict_slashes=False)
def contacts():
    """contact us page"""
    return render_template("contacts.html")


@app_views.route("/feedback", methods=['POST'], strict_slashes=False)
def user_message():
    """handle user feedback"""
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return "Thank you for feedback"


@app_views.route("/county/service", methods=['POST'], strict_slashes=False)
def render_service():
    """handle service request"""
    service = request.form.get('service')
    county = session.get('county')
    # if service == "" or service == None:
     #   return render_template("choose.html", name=county)
    
    county_list = County.query.all()
    countyid = next((obj.id for obj in county_list if obj.name == county), None)
    
    service_class = service_classes.get(service)
    service_vendors = service_class.query.all()
    service_list = []
    for vendor in service_vendors:
        if vendor.county_id == countyid:
            service_list.append(vendor)
    if len(service_list) == 0:
        return render_template("no_service.html", county=county)
    return render_template(
            "service_list.html", service_list=service_list, county=county, service=service.capitalize())


@app_views.route("/weather", strict_slashes=False)
def weather():
    "get city in Kenya"
    return render_template("weather.html")


@app_views.route("/weather_service", methods=['GET'], strict_slashes=False)
def serve_weather():
    """serve weather for town in Kenya"""
    city = request.args['city']
    try:
         response = requests.get(
                 f'http://api.openweathermap.org/data/2.5/weather?q={city},kenya&units=metric&APPID=afa5700d7e39ac5d8cb0353f688e020b')
    except Exception as e:
        return "Town / city not found"

    weather = response.json()
    temperature = weather['main']['temp']
    clouds = weather['weather'][0]['description']
    humidity = weather['main']['humidity']
    wind = weather['wind']['speed']
    return render_template(
            "weather_service.html", temperature=temperature, clouds=clouds, humidity=humidity, wind=wind, city=city)
