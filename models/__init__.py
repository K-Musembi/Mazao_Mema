from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

from app.models.county import County
from app.models.consultant import Consultant
from app.models.input_dealer import InputDealer
from app.models.buyer import Buyer
