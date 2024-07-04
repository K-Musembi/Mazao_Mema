#!/usr/bin/python3
"""input-dealer model module"""

from models import db
from models.base_model import BaseModel


class InputDealer(BaseModel):
    """input dealer class"""
    __tablename__ = "input_dealer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey("county.id"), nullable=False)
    location = db.Column(db.String(50))
    contact = db.Column(db.String(50))
    products_offered = db.Column(db.String(100))

    def __init__(self, name, county_id, location, contact, products_offered=None):
        """initialize object"""
        self.name = name
        self.county_id = county_id
        self.location = location
        self.contact = contact
        self.products_offered = products_offered

    def __str__(self):
        """string representation"""
        return "inputdealer object"
