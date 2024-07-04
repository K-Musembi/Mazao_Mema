#!/usr/bin/python3
"""county model module"""

from models import db
from models.base_model import BaseModel


class County(BaseModel):
    """county objects"""
    __tablename__ = "county"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        """initialize objects"""
        self.name = name

    def __str__(self):
        """string representation"""
        return "county object"
