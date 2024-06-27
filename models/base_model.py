#!/usr/bin/python3
"""Base model module"""

from app.models import db

class BaseModel(db.Model):
    """Base model class"""
    __abstract__ = True

    def add(self):
        """add object to db"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """delete object from db"""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls):
        """retreve all objects"""
        return cls.query.all()
