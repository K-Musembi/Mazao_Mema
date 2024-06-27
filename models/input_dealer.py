#!/usr/bin/python3
"""input-dealer model module"""

from app.models import db
from app.models.base_model import BaseModel


class InputDealer(BaseModel):
    """input dealer class"""
    __tablename__ = "input_dealer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey("county.id"), nullable=False)
    location = db.Column(db.String(50))
    contact = db.Column(db.String(50))
    products_offered = db.Column(db.String(100))
