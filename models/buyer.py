#!/usr/bin/python3
"""buyer model module"""

from models import db
from models.base_model import BaseModel


class Buyer(BaseModel):
    """buyer objects"""
    __tablename__ = "buyer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey("county.id"), nullable=False)
    contact = db.Column(db.String(50))
    products = db.Column(db.String(100))

    def __init__(self, name, county_id, contact, products=None):
        """initialize objects"""
        self.name = name
        self.county_id = county_id
        self.contact = contact
        self.products = products

    def __str__(self):
        """string representation"""
        return "buyer object"
