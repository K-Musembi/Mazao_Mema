#!/usr/bin/python3
"""consultant model module"""

from models import db
from models.base_model import BaseModel


class Consultant(BaseModel):
    """consultant objects"""
    __tablename__ = "consultant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey("county.id"), nullable=False)
    contact = db.Column(db.String(50))
    services_offered = db.Column(db.String(50))

    def __init__(self, name, county_id, contact, services_offered=None):
        """initialize objects"""
        self.name = name
        self.county_id = county_id
        self.contact = contact
        self.services_offered = services_offered

    def __str__(self):
        """string representation"""
        return "consultant object"
