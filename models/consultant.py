#!/usr/bin/python3
"""consultant model module"""

from app.models import db
from app.models.base_model import BaseModel


class Consultant(BaseModel):
    """consultant objects"""
    __tablename__ = "consultant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey("county.id"), nullable=False)
    contact = db.Column(db.String(50))
    services_offered = db.Column(db.String(50))

    def __init__(self, name, contact, services_offered=None):
        """initialize objects"""
        self.name = name
        self.contact = contact
        self.services_offered = services_offered
